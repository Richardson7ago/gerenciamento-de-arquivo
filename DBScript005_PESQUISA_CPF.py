# -*- coding: utf-8 -*-

import sqlite3

def mostrar():
    conn = sqlite3.connect('arquivo_cdra')
    curs = conn.cursor()
    consulta = input('Digite o número do CPF: \n>>>')
    curs.execute("""
    SELECT * FROM ALUNOS WHERE CPF='%s';
                 \n""" % (consulta))
    for linha in curs.fetchall():
        print('*'*80)
        print('\n\nID: ', linha[0], '\n\nCPF: ', linha[1], '\n\nNome: ', linha[2],'\n\nBox: ', linha[3], '\n\nCódigo: ', linha[4], '\n\n')
        print('*'*80)
        conn.close()
try:
    while True:
        mostrar()
        print('PRESS CTRL + C PARA SAIR...\n\n')
except:
    print('ERRO MSG!!!')
