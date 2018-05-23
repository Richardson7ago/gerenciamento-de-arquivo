# -*- coding: utf-8 -*-
import sqlite3

def mostra_todos():
    conn = sqlite3.connect('arquivo_cdra')
    curs = conn.cursor()
    curs.execute('select * from alunos')
    count = 0
    for linha in curs.fetchall():
        count = count + 1
        print('ID: ', linha[0], 'CPF: ', linha[1], 'Nome: ', linha[2], 'Box: ', linha[3], 'Código: ', linha[4])
    conn.close()
    print('QUANTIDADE DE REGISTROS: ', count)

def atualiza_dados():
    conn = sqlite3.connect('arquivo_cdra')
    curs = conn.cursor()
    curs.execute('select * from alunos')
    count = 0
    for linha in curs.fetchall():
        count = count + 1
    curs.execute("""update alunos set nome = "Joana D'arc de Souza Oliveira" where id = 1901""")
    print('Registro atualizado com sucesso!!')
    print('QUANTIDADE DE REGISTROS: ', count)
    print('\n\n')
    print('ULTIMO REGISTRO:\n\n', 'ID: ', linha[0], 'CPF: ', linha[1], 'Nome: ', linha[2], 'Box: ', linha[3], 'Código: ', linha[4],'\n\n')
    conn.commit()
    conn.close()


try:
    while True:
        tentativa = input("Digite '1' para mostrar todos os dados ou '2' para atualizar:\n>>>")
        if tentativa == str(1):
            mostra_todos()
        else:
            atualiza_dados()
except:
    print('Entrar em contato com o programador...')