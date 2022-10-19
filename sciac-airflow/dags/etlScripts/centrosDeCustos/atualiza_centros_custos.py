# Importando as Bibliotecas necessárias
from cmath import log
import json
import logging
from neo4j import GraphDatabase 

# Obtendo os dados no arquivo temporário
logging.info('Obtendo os dados armazenados no arquivo temporário pela tarefa anterior')
file = '/usr/local/airflow/dags/etlScripts/tempFiles/centros_de_custos_temp.txt'
with open(file,'r') as temp_file: 

    # Lendo os dados e armazenando em uma variável json
    json_data = json.load(temp_file)
    temp_file.close()

# Estabelece a conexão com o banco de dados e obtém os centros de custos ativos nele armazenados
logging.info('Obtendo os Centros de Custos ativos armazenados na base')

# Conectando-se ao banco de dados
# Credenciais de acesso ao banco
uri = 'neo4j+s://1258ca96.databases.neo4j.io'
user = 'neo4j'
password = 'vay_x2AgwSbsGxbulFpGtJDzAjSo1JnwF_6mVhqPbrU'

grafo = GraphDatabase.driver(uri, auth=(user, password))
grafo

# Obtém os centros de custos ativos na base
session=grafo.session()
q1="MATCH (n) RETURN (n)"
nodes=session.run(q1)
print('Os nós encontrados foram:')
for node in nodes:
    print(node)


grafo.close()

# Processa os dados
logging.info('Processando os dados, tratando as atualizações necessárias')

# Grava as atualizações e fecha o arquivo
logging.info('Gravando as alterações no arquivo temporário')


logging.info('Centros de Custos atualizados com sucesso!')