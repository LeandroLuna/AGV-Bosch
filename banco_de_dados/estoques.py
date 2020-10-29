#!/usr/bin/env python3
import time

# Importa o conector mariadb e seus devidos modulos
import mysql.connector as mariadb
import mysql.connector

# Estabelece a conexao com banco de dados
db = mariadb.connect(user="lunaa",
                     host="localhost",
                     password="4352",
                     database="estoques"
                     )

cursor = db.cursor()
pos = 1
p = []
x = 0


def posicao(x, pos):  # funcao para calcular a posicao a ser colocado o produto
    pst = 'SELECT posicao FROM {}'.format(tipo_produto.lower())
    cursor.execute(pst)
    #cursor.execute("SELECT posicao FROM freios")
    posicao_db = cursor.fetchall()
    for i in posicao_db:
        positions = list(i)
        p.append(positions[0])
    ext_pos = len(p)
    position = sorted(p)
    while x < ext_pos:
        if pos == position[x]:
            pos += 1
        else:
            pass
        x += 1
    return pos

#cursor.execute("DROP TABLE IF EXISTS ifm")


resp = 'sim'
while resp == 'sim':
    tipo_produto = raw_input(
        "Informe a categoria do tipo do produto a ser inserido no banco de dados: \n\n\t1.Freios\n\t2.Filtros\n\t3.Baterias\n\n*Escreva por extenso: ")
    if tipo_produto == 'Freios':
        # cursor.execute("CREATE TABLE freios(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
        #				"nome TEXT,"
        #				"posicao TINYINT,"
        #				"data TEXT)")
        nome = raw_input("Informe o nome para identificacao do produto: ")
        data = time.strftime('%Y-%m-%d %H:%M:%S')
        posicao(x, pos)
        dados = (nome, posicao(x, pos), data)
        print 'Posicao livre no estoque {}: {}'.format(tipo_produto, dados[1])
        cursor.execute(
            "INSERT INTO freios(id, nome, posicao, data) VALUES (NULL, %s, %s, %s);", dados)
        db.commit()
        print('Informacoes inseridas com sucesso!')
        resp = 'nao'

    elif tipo_produto == 'Filtros':
        nome = raw_input("Informe o nome para identificacao do produto: ")
        data = time.strftime('%Y-%m-%d %H:%M:%S')
        posicao(x, pos)
        dados = (nome, posicao(x, pos), data)
        print 'Posicao livre no estoque {}: {}'.format(tipo_produto, dados[1])
        cursor.execute(
            "INSERT INTO filtros(id, nome, posicao, data) VALUES (NULL, %s, %s, %s);", dados)
        db.commit()
        print('Informacoes inseridas com sucesso!')
        resp = 'nao'

    elif tipo_produto == 'Baterias':
        # cursor.execute("CREATE TABLE baterias(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
        #				"nome TEXT,"
        #				"posicao TINYINT,"
        #				"data TEXT)")
        nome = raw_input("Informe o nome para identificacao do produto: ")
        data = time.strftime('%Y-%m-%d %H:%M:%S')
        posicao(x, pos)
        dados = (nome, posicao(x, pos), data)
        print 'Posicao livre no estoque {}: {}'.format(tipo_produto, dados[1])
        cursor.execute(
            "INSERT INTO baterias(id, nome, posicao, data) VALUES (NULL, %s, %s, %s);", dados)
        db.commit()
        print('Informacoes inseridas com sucesso!')
        resp = 'nao'

    else:
        print('A categoria do produto informada nao consta no banco de dados. Por favor, insira uma categoria valida.')
        resp = raw_input(
            'Quer reiniciar o programa? Responda com "sim" ou "nao":\n')

cursor.close()
db.close()
