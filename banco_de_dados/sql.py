import sqlite3
# from qrcode_rfid import *

ID = input('Informe o ID do produto: ')
Local = input('Informe a localizaçao do produto: ')

conexao = sqlite3.connect('estoques.db')
cursor = conexao.cursor()
cursor.execute('create table estoques(ID text, Localização text)')
cursor.execute(
    'insert into estoques(ID, Localização) values (?,?)', (ID, Local))
conexao.commit()

cursor.close()
conexao.close()
