### Packages for UI ###
from .form import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem

### Packages for Main ###
import sys, os

sys.path.append("..")
from controllers.labeling import *
from models.db import Database
from pydub import AudioSegment
from datetime import datetime


DATASET = os.path.join('..', '..', 'dataset', 'origin')
FLUSH_DIR = os.path.join('..', '..', 'dataset', 'flush_'+datetime.today().strftime("%Y%m%d"))
ROOT_DIR = os.path.abspath(DATASET)
PATH_LOC = os.path.join('labels', 'location.yaml')

LOCAT_CODE = {"Taiwan": "TW", "Hsinchu": "HC", "Taipei": "TPE",
			"Japan": "JP", "Osaka": "OSK", "Tokyo": "TK"}

class MainWindow(QMainWindow):
	def __init__(self, mode):
		super().__init__()
		self.mode = mode
		self.initDB()
		self.initUI()

	def initUI(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.btn_load.clicked.connect(self.loadData)

		if self.mode == "init":
			self.ui.btn_save.clicked.connect(self.parseData)

		elif self.mode == "load":
			# load flushed data
			dir_path = ROOT_DIR.replace("origin", "flush_20200722")
			self.ui.textbox_root.setText(dir_path)
			self.resetRoot(dir_path)

			self.ui.btn_save.clicked.connect(self.updateData)
		
		self.ui.textbox_root.returnPressed.connect(self.loadData)
		self.ui.tree_dataset.selectionModel().selectionChanged.connect(self.loadAudioFile)
		#self.ui.tree_dataset.doubleClicked.connect(self.loadAudioFile)
		#self.ui.textbox_root.textChanged.connect(self.resetRoot)
		#self.ui.tree_dataset.selectionModel().selectionChanged.connect(self.load_labeldata)

		self.loadLabel()

	def initDB(self):
		self.db = Database()
		self.db.createDB()

	def loadLabel(self):
		loc_dict = load_from_yaml(PATH_LOC)
		for loc in loc_dict['location']:
			self.ui.combo_location.addItem(loc['country']+' / '+loc['city'])

		for place in loc_dict['place']:
			item = QListWidgetItem()
			item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
			item.setCheckState(Qt.Unchecked)
			item.setText(place)        	
			self.ui.list_location.addItem(item)

	def loadData(self):
		if self.ui.textbox_root.text() == '':
			self.ui.textbox_root.setText(ROOT_DIR)
			self.ui.model_dataset.setRootPath(ROOT_DIR)
			self.ui.tree_dataset.setRootIndex(self.ui.model_dataset.index(ROOT_DIR))
		else:
			self.resetRoot(self.ui.textbox_root.text())

	def parseData(self):
		if not os.path.exists(FLUSH_DIR): os.mkdir(FLUSH_DIR)

		try:
			audio = AudioSegment.from_file(self.file_path)
			loc = self.ui.combo_location.currentText().split(' / ')
			#fid = self.db.getCountFromTable("Recording")
			fid = self.db.queryFromTable("Recording", {'country': loc[0], "city": loc[1]})
			fname = LOCAT_CODE[loc[0]]+'_'+LOCAT_CODE[loc[1]]+'_%.3d' %(fid+1) +'.wav'

			datetime_str = self.ui.textbox_timestamp.text()
			print('>>> Save as', fname)
			
			try:
				if " " in datetime_str:
					datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H%M%S').strftime('%Y-%m-%d %H:%M:%S')
				else: 
					datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d')
				
				# Export as WAV
				audio.export(os.path.join(FLUSH_DIR, fname), format='wav')
				os.remove(self.file_path)

				# Commit to DB
				self.db.insertDB("Recording", {
						"filename": fname,
						"length": audio.duration_seconds,
						"description": self.ui.textbox_description.text(),
						"country": loc[0],
						"city": loc[1],
						"place": None,
						"soundsource": None,
						"timestamp": datetime_object
					})

				# Clear data
				self.ui.textbox_description.clear()
				self.ui.textbox_timestamp.clear()
				for idx in range(self.ui.list_location.count()):
					item = self.ui.list_location.item(idx)
					if item.checkState() == Qt.Checked:
						item.setCheckState(Qt.Unchecked)
				print('>>> Done!\n')
			except ValueError as ve:
				print('ValueError Raised:', ve)
		
		except AttributeError as ae:
			print('FileNotExistError Raised: This is not an audio file')
		

	def updateData(self):
		print('>>> Update', self.record['filename'])
		loc = self.ui.combo_location.currentText().split(' / ')
		self.db.updateDB("Recording", {
				"id": self.record['id'],
				"description": self.ui.textbox_description.text(),
				"country": loc[0],
				"city": loc[1],
				"place": None,
				"soundsource": None
			})


	def loadAudioFile(self):
		if self.ui.tree_dataset.selectedIndexes():
			idx = self.ui.tree_dataset.selectedIndexes()[0]
			crawler = idx.model().itemData(idx)
			#crawler = idx.model().filePath(idx)

			if any(ftype in crawler[0] for ftype in ['.mp3', '.wav', '.WAV', '.m4a']):
				print('>>> Load', crawler[0])
				self.file_path = idx.model().filePath(idx)

				if self.mode == "init":
					# Parse origin filename to description
					fspilt = self.file_path.split('/')
					self.ui.textbox_description.setText(fspilt[-1].split('.')[0])

					# Parse datetime from folder
					date = fspilt[-2]
					datetime_object = datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
					self.ui.textbox_timestamp.setText(datetime_object)

					# Parse location from folder
					combo_item = fspilt[-4] + ' / ' + fspilt[-3]
					combo_idx = self.ui.combo_location.findText(combo_item, Qt.MatchFixedString)
					if combo_idx >= 0:
						self.ui.combo_location.setCurrentIndex(combo_idx)

				elif self.mode == "load":
					self.record = self.db.queryFromTable("Recording", {'filename': crawler[0]})

					# Parse from DB
					# description
					self.ui.textbox_description.setText(self.record['description'])
					# timestamp
					self.ui.textbox_timestamp.setText(str(self.record['timestamp']))
					# location
					combo_item = self.record['country'] + ' / ' + self.record['city']
					combo_idx = self.ui.combo_location.findText(combo_item, Qt.MatchFixedString)
					if combo_idx >= 0:
						self.ui.combo_location.setCurrentIndex(combo_idx)

			else:
				print('Load', crawler[0])
		

	def resetRoot(self, dir_path):
		#ROOT_DIR = self.ui.textbox_root.text()
		self.ui.model_dataset.setRootPath(dir_path)
		self.ui.tree_dataset.setRootIndex(self.ui.model_dataset.index(dir_path))