FROM puckel/docker-airflow


WORKDIR ${AIRFLOW_USER_HOME}

COPY airflow.cfg ./airflow.cfg
COPY dags ./dags

RUN pip install neo4j

EXPOSE 8080 5555 8793

CMD ["webserver"]