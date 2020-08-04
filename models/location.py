class Location():
	table_name = 'Location'

	def __init__(self):
		pass

	def createTable(self):
		return """
			CREATE TABLE `Location`
			(
			 `id`      varchar(3) NOT NULL ,
			 `country` varchar(100) NOT NULL ,
			 `city`    varchar(100) NOT NULL ,
			 `place`   varchar(100) NOT NULL UNIQUE,

			PRIMARY KEY (`id`)
			);
			"""
