# gerenciamento-de-arquivo
Este é um programa escrito em python para solucionar um problema simples de arquivo.
Foi adotada a seguinte estrutura de armazenamento:
Um arquivo.
Dentro do arquivo uma tabela chamada alunos.
Dentro da tabela alunos foram inseridos 5 campos, são eles: id, cpf, nome, box e codigo.
O id segue a ordem de inserção dentro do banco de dados, ou seja, de 1 a n.
O cpf não se repete e segue a estrutura '000.111.000-12'.
O nome é qualquer variação de texto, exemplo: 'João da Silva'.
o box segue uma estrutura alfa numérica, da seguinte forma: inicia-se em A1 e vai de do código 02-001 a 02-200, A2 que vai do código 02-201 a 02-400, A3 que vai de 02-401 a 02-600 e assim sucessivamente até chegar em A10. Dái segue para B, C, D, E, seguindo a mesma lógica anterior, ou seja, de 200 em 200 muda-se o box.
o código segue a seguência 02, seguida do id. Ex: 02-001, 02-002, 02-6573 e assim por diante.
Possui funções de criação, de inserção, de atualização, de geração de arquivo csv o qual está vinculado a um documento word o qual trata-se da impressão das etiquetas que vão ser coladas nas pastas dos alunos, onde todos os documentos referentes àquele aluno são devidmente arquivadas.  
