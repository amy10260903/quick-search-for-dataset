import pymysql
from .recording import Recording
from .location import Location
from .soundsource import Soundsource

import sys
sys.path.append("..")
from config import Config

class Database():
	def __init__(self):

		self.con = pymysql.connect(
			host=Config.SQL_DATABASE_HOST, 
			user=Config.SQL_DATABASE_USER, 
			password=Config.SQL_DATABASE_PWD, 
			db=Config.SQL_DATABASE_NAME, 
			cursorclass=pymysql.cursors.DictCursor)
		
		self.cur = self.con.cursor()

	def createDB(self):
		self.table_list = {}
		self.table_list[Recording.table_name] = Recording()
		self.table_list[Location.table_name] = Location()
		self.table_list[Soundsource.table_name] = Soundsource()

		for name, obj in self.table_list.items():
			try:
				self.cur.execute(obj.createTable())
			except pymysql.OperationalError as e:
				continue
				#print('OperationalError: ', e.args[1])

	def insertDB(self, table_name, data):
		if table_name == "Recording":
			record = self.table_list[Recording.table_name]
			self.cur.execute(record.insertTable(), (
				data['filename'], 
				data['length'], 
				data['description'],
				data['country'],
				data['city'], 
				data['place'],
				data['soundsource'],
				data['timestamp']))
			self.con.commit()

	def updateDB(self, table_name, data):
		if table_name == "Recording":
			record = self.table_list[Recording.table_name]
			self.cur.execute(record.updateTable(), (
				data['description'],
				data['country'],
				data['city'], 
				data['place'],
				data['soundsource'],
				data['id']))
			self.con.commit()

	def getCountFromTable(self, table_name):
		if table_name == "Recording":
			record = self.table_list[Recording.table_name]
			self.cur.execute(record.getLastItem())
			id = self.cur.fetchone()
			if id:
				return id['id']
			else:
				return 0

	def queryFromTable(self, table_name, data):
		if table_name == "Recording":
			record = self.table_list[Recording.table_name]
			if 'filename' in data.keys():
				self.cur.execute(record.queryItem(), data['filename'])
				crawler = self.cur.fetchone()
				return crawler
			else:
				self.cur.execute(record.queryGroup(), (data['country'], data['city']))
				crawler = self.cur.fetchall()
				return len(crawler)






		