class Soundsource():
	table_name = 'Soundsource'

	def __init__(self):
		pass

	def createTable(self):
		return """
			CREATE TABLE `Soundsource`
			(
			 `id`       varchar(2) NOT NULL ,
			 `category` varchar(100) NOT NULL ,
			 `sound`    varchar(100) NOT NULL ,

			PRIMARY KEY (`id`)
			);
			"""
