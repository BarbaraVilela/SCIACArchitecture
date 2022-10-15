# Importando as Bibliotecas necessárias
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator

# Definindo alguns argumentos básicos
default_args = {
   'owner': 'Bárbara Vilela',
   'depends_on_past': False,
   'start_date': datetime(2022, 1, 1),
   'email': ['pucprojeto.sciac@hotmail.com'],
   'email_on_failure': ['pucprojeto.sciac@hotmail.com'],
   'retries': 0,
   }
   
# Nomeando a DAG e definindo quando será executada
with DAG(
   'dag_carga_centros_custos',
   schedule_interval=timedelta(hours=6),
   catchup=False,
   default_args=default_args
   ) as dag:   

   # Definindo as tarefas a serem executadas

   buscaDados = BashOperator(
      task_id='busca_centros_custos',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etlScripts/centrosDeCustos/
      python3 busca_centros_custos.py
      """)

   atualizaDados = BashOperator(
      task_id='atualiza_centros_custos',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etlScripts/centrosDeCustos/
      python3 atualiza_centros_custos.py
      """)

   carregaDados = BashOperator(
      task_id='carrega_centros_custos',
      bash_command="""
      cd $AIRFLOW_HOME/dags/etlScripts/centrosDeCustos/
      python3 carrega_centros_custos.py
      """)

   notifica = EmailOperator(
    task_id='send_email',
    to='pucprojeto.sciac@hotmail.com',
    subject='Carga completa',
    html_content="Date: {{ ds }}")

   # Definindo o padrão de execução
   buscaDados >> atualizaDados >> carregaDados >> notifica