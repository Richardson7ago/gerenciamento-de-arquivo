# -*- coding: utf-8 -*-

import sqlite3

def gerar_csv():
    conn = sqlite3.connect('arquivo_cdra')
    curs = conn.cursor()
    curs.execute('select * from alunos')
    count = 0
    with open('etiquetas.csv', 'w', newline='', encoding='utf-8') as f:
        f.write('id,')
        f.write('cpf,')
        f.write('nome,')
        f.write('box,')
        f.write('codigo')
        f.write('\n')
        for linha in curs.fetchall():
            f.write(str(linha[0]))
            f.write(',')
            f.write(linha[1])
            f.write(',')
            f.write(linha[2])
            f.write(',')
            f.write(linha[3])
            f.write(',')
            f.write(linha[4])
            f.write('\n')
            count = count + 1
            conn.close()
        print('Total de Registro Copiados: ', count)    

gerar_csv()


