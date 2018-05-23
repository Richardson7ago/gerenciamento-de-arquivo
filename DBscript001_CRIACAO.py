# -*- coding: utf-8 -*-
import sqlite3


conn = sqlite3.connect('arquivo_cdra')
curs = conn.cursor()

tblcmd = """
create table alunos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cpf VARCHAR(11) NOT NULL,
	   nome TEXT NOT NULL,
	   box TEXT,
	   codigo TEXT
);
"""

curs.execute(tblcmd)
conn.commit()
print('Arquivo criado com sucesso!!!')
conn.close()

#arquivo executado no dia 06/12/2017 para criação do arquivo de nome 'arquivo_cdra'

