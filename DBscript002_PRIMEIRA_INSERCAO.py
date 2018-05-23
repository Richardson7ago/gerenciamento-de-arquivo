# -*- coding: latin1 -*-
import sqlite3
import csv


conn = sqlite3.connect('arquivo_cdra')
curs = conn.cursor()


with open('dados_atuais.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cpf, nome = row['CPF'], row['Nome']
        curs.execute('insert into alunos values (null, ?, ?, null, null)', (cpf,nome))
        print('CPF: ',cpf,' ', 'Nome: ', nome,'- Inserido com Sucesso!!!')
               
conn.commit()
conn.close()
