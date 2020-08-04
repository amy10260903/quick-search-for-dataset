### Packages for UI ###
from .form import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QAbstractItemView

### Packages for Main ###
import json
import sys, os

sys.path.append("..")
from controllers.labeling import *
from models.db import Database

PATH_LABEL = os.path.join('labels', 'ontology.json')
PATH_LOC = os.path.join('labels', 'location.yaml')

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initDB()
		self.initUI()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Backspace:
			self._del_item()

	def _del_item(self):
		if self.ui.list_soundsource.selectedItems():
			for item in self.ui.list_soundsource.selectedItems():
				self.ui.list_soundsource.takeItem(self.ui.list_soundsource.row(item))

	def _add_item(self):
		if self.ui.list_location.count() == 0:
			item = QListWidgetItem()
			item.setFlags(item.flags() | Qt.ItemIsEditable)
			self.ui.list_location.addItem(item)
		else:
			count = self.ui.list_location.count()
			itemlist = []
			for idx in range(count-1):
				if self.ui.list_location.item(idx).text() == "":
					self.ui.list_location.takeItem(idx)
					count -= 1
			
			item = self.ui.list_location.item(count-1)
			if item.text():
				item = QListWidgetItem()
				item.setFlags(item.flags() | Qt.ItemIsEditable)
				self.ui.list_location.addItem(item)
			else:
				pass

	def initUI(self):
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.load()

		self.ui.btn_load.clicked.connect(self.load)
		self.ui.btn_save.clicked.connect(self.save)

		## Drag and drop
		#self.ui.list_location.setDragDropMode(QAbstractItemView.DropOnly)
		self.ui.list_soundsource.setDragDropMode(QAbstractItemView.DropOnly)
		self.ui.tree_dataset.setDragDropMode(QAbstractItemView.DragOnly)
		
		# Add item in listwidget
		self._add_item()
		#self.ui.list_location.itemSelectionChanged.connect(self.addItem)
		self.ui.list_location.itemChanged.connect(self._add_item)

	def initDB(self):
		self.db = Database()
		self.db.createDB()

	def save(self):
		list_label = {}
		list_location = []
		list_soundsource = []
		for idx in range(self.ui.list_location.count()):
			item = self.ui.list_location.item(idx)
			if not item.text() == '':
				list_location.append(item.text())

		for idx in range(self.ui.list_soundsource.count()):
			item = self.ui.list_soundsource.item(idx)
			if not item.text() == '':
				list_soundsource.append(item.text())

		list_label['place'] = list_location
		list_label['soundsource'] = list_soundsource

		save_into_yaml(PATH_LOC, list_label)

	def load(self):
		self.loadData()
		self.loadLabel()

	def loadLabel(self):
		# Refresh the list
		self.ui.list_location.clear()

		# Load from yaml
		loc_dict = load_from_yaml(PATH_LOC)

		for key, value in loc_dict.items():
			if not value == None:
				if key == 'location':
					for loc in loc_dict['location']:
						self.ui.combo_location.addItem(loc['country']+' / '+loc['city'])
				
				elif key == 'place':
					for place in loc_dict['place']:
						item = QListWidgetItem()
						item.setFlags(item.flags() | Qt.ItemIsEditable)
						item.setText(place)        	
						self.ui.list_location.addItem(item)

				elif key == 'soundsource':
					for sound in loc_dict['soundsource']:
						item = QListWidgetItem()
						item.setText(sound)
						self.ui.list_soundsource.addItem(item)

		self.ui.list_location.setSortingEnabled(True)
		self.ui.list_location.sortItems(Qt.DescendingOrder)
		self._add_item()

	def loadData(self):
		# Refresh the model
		self.ui.model_dataset.removeRows(0, self.ui.model_dataset.rowCount())

		# Load from json
		load_from_json(PATH_LABEL, self.ui.root_node)
		
		self.ui.tree_dataset.setModel(self.ui.model_dataset)
		self.ui.tree_dataset.expandAll()
		self.ui.tree_dataset.setSortingEnabled(True)
		self.ui.tree_dataset.sortByColumn(0, Qt.AscendingOrder)      

	def saveData(self):
		pass

