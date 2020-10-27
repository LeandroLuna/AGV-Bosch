#!/usr/bin/env python3
from datetime import date
import time
import datetime
import sys
import os

# Import MariaDB Connector/Python module
import mysql.connector as mariadb
import mysql.connector
# Establish a connection
db = mariadb.connect(user="lunaa",
                            host="localhost",
                            password="4352",
                            database="estoques"
							)

cursor= db.cursor()

#cursor.execute("DROP TABLE IF EXISTS baterias")
#cursor.execute("CREATE TABLE baterias(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
#				"nome TEXT,"
#				"posicao TINYINT,"
#				"data TEXT)")
#dados = ['mourasss', '1', '27/10/2020']
cursor.execute("INSERT INTO baterias(id, nome, posicao, data) VALUES (NULL, 'mourasss', '1', '27/10/2020');")
db.commit()
# retrieve data
#cursor.execute("SELECT id, nome, posicao, data FROM baterias")
print('ok')
time.sleep(2)		

#sql = "SELECT * FROM baterias"
#cursor.execute(sql)
#linhas = cursor.fetchall()

cursor.execute("SELECT posicao FROM baterias")
linhas = cursor.fetchall()
print(linhas)
	
		
cursor.close()
db.close()
