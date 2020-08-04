class Recording():
	table_name = 'Recording'
	
	def __init__(self):
		pass

	def createTable(self):
		return """
			CREATE TABLE `Recording`
			(
			 `id`          integer NOT NULL AUTO_INCREMENT ,
			 `filename`    varchar(100) NOT NULL ,
			 `length`      varchar(100) NOT NULL ,
			 `description` varchar(255) NULL ,
			 `country`     varchar(100) NOT NULL,
			 `city`        varchar(100) NOT NULL,
			 `place`       varchar(100) NULL,
			 `soundsource` json NULL ,
			 `timestamp`   datetime NOT NULL ,

			PRIMARY KEY (`id`)
			);
			"""

	def insertTable(self):
		return """
			INSERT INTO `Recording` 
			(`filename`, `length`, `description`, `country`, `city`, `place`, `soundsource`, `timestamp`) 
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
			"""

	def updateTable(self):
		return """
			UPDATE `Recording` SET 
			description = %s,
			country = %s, 
			city = %s,
			place = %s,
			soundsource = %s
			WHERE id = %s;
			"""

	def getLastItem(self):
		return """
			SELECT * from `Recording`
			WHERE id=(
				SELECT MAX(id) FROM `Recording`
			);
			"""
	
	def queryItem(self):
		return """
			SELECT * from `Recording`
			WHERE filename = %s;
			"""

	def queryGroup(self):
		return """
			SELECT * from `Recording`
			WHERE country=%s and city=%s;
			"""