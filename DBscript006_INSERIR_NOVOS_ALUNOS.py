# -*- coding: UTF-8 -*-
import sqlite3
import csv


conn = sqlite3.connect('arquivo_cdra')
curs = conn.cursor()
filename = input('digite aqui o nome do arquivo\n>>>')

arquivo = 'transcrito.csv'
with open(arquivo, 'w') as novo:
    with open(filename, newline='', encoding='utf-8') as f:
        lista = []
        for linha in f:
            lista.append(linha)
        lista_nova = lista[2:]
        for i in lista_nova:
            novo.write(i)
        
        
            

with open('transcrito.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cpf, nome = row['CPF'], row['Nome']
        sql = "select cpf from alunos where cpf = '%s'" % cpf
        curs.execute(sql)
        if len(curs.fetchall()) >=1 and len(cpf)==14:
            print('Dado j? constante do banco de dados....')
        else:
            curs.execute('insert into alunos values (null,?,?,null,null)', (cpf, nome))
            print('CPF: %s - Nome: %s - Inserido com Sucesso!' % (cpf, nome))

curs.execute('select cpf from alunos')
print('Total de dados inseridos no banco de dados: ', len(curs.fetchall()))
                
conn.commit()
conn.close()

