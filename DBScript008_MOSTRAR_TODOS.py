# -*- coding: utf-8 -*-

import sqlite3

def mostrar():
    conn = sqlite3.connect('arquivo_cdra')
    curs = conn.cursor()
    curs.execute('select * from alunos')
    count = 0
    for linha in curs.fetchall():
        count = count + 1
        print('ID: ', linha[0], 'CPF: ', linha[1], 'Nome: ', linha[2], 'Box: ', linha[3], 'Código: ', linha[4])
        conn.close()
    print('Total de Dados: ', count)
    print('\n\n')    

try:
    mostrar()
    print('Execução realizada com sucesso!!!\n\n')
except:
    print('Entrar em contato com o programador...')
