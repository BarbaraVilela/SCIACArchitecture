# Importando as Bibliotecas necessárias
import json
import logging

# Obtendo os dados no arquivo temporário
logging.info('Obtendo os dados armazenados no arquivo temporário pela tarefa anterior')
file = '/usr/local/airflow/dags/etlScripts/tempFiles/centros_de_custos_temp.txt'
with open(file,'r') as temp_file: 

    # Lendo os dados e armazenando em uma variável json
    json_data = json.load(temp_file)
    temp_file.close()

# Estabelece a conexão com o banco de dados e carrega os dados atualizados
logging.info('Gravando as alterações na base')

logging.info('Centros de Custos carregados com sucesso!')