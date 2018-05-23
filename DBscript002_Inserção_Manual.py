# -*- coding: utf8 -*-
import sqlite3

def Inserir_Dados_Arquivo(cpf, nome):
    conn = sqlite3.connect('arquivo_cdra')
    curs = conn.cursor()
    curs.execute('insert into alunos values (null, ?, ?, null, null)', (cpf,nome))
    print('CPF: ',cpf,' ', 'Nome: ', nome,'- Inserido com Sucesso!!!')
    conn.commit()
    conn.close()
	
	
	
#Inserir_Dados_Arquivo('cpf','nome')



def Verificar_Inserir_Dados_Arquivo(cpf, nome):
    conn = sqlite3.connect('arquivo_cdra')
    curs = conn.cursor()
    sql = "select cpf from alunos where cpf = '%s'" % cpf
    curs.execute(sql)
    if len(curs.fetchall()) >=1 and len(cpf)==14:
        print('Dados já constantes no banco de dados....')
    else:
        curs.execute('insert into alunos values (null,?,?,null,null)', (cpf, nome))
        print('CPF: %s - Nome: %s - Inserido com Sucesso!' % (cpf, nome))
    curs.execute('select cpf from alunos')
    print('Total de dados inseridos no banco de dados: ', len(curs.fetchall()))
    conn.commit()
    conn.close()

Verificar_Inserir_Dados_Arquivo('000.111.222-33','Fulano de Tal')
