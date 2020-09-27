import sqlite3
# from qrcode_rfid import *

ID = input('Informe o ID do produto: ')
Local = input('Informe a localizaçao do produto: ')

conexao = sqlite3.connect('estoques.db')
cursor = conexao.cursor()
#cursor.execute('create table estoques(ID integer, Local text)')
cursor.execute(
    'insert into estoques(ID, Local) values (?,?)', (ID, Local))
conexao.commit()
cursor.execute('SELECT * FROM estoques')
estoque_apresentar = cursor.fetchall()

for banco_dados in estoque_apresentar:
    print('ID: %s \nLocalizaçao: %s' % (estoque_apresentar))

cursor.close()
conexao.close()
