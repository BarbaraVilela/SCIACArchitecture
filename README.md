# SCIACArchitecture
O projeto SCIACArchitecture apresenta a implementação de um protótipo de arqitetura proposta para um Sistema de Coleta, Integração e Análises de informações de Custos - SCIAC, a ser desenvolvido em um órgão do Executivo Municipal da esfera pública brasileira.
O SCIAC tem como principais objetivos a coleta de dados de custos relativos ao município, a integração deles em torno dos Centros de Custos por eles responsáveis e a alimentação de uma base de dados unificada, de onde poderão ser geradas informações robustas a serem analisadas posteriormente. Essa base será utilizada para análises de cunho gerencial e fiscalizatório, garantindo uma fonte de informações valiosa para a tomada de decisões por parte dos gestores públicos.
Para atender a esses propósitos, construiu-se um protótipo da aplicação, contemplando os principais módulos nela envolvidos, que serão detalhados a seguir.
Essa construção atende ao projeto de conclusão do curso de Pós-Graduação Latto sensu em Arquitetura de Softwares Distribuídos, ofertado pela PUCMinas Virtual. O relatório completo, contendo os detalhes da arquitetura proposta, sua modelagem segundo o modelo C4 e as considerações finais pode ser encontrado no arquivo "RelatórioTécnico.pdf", disponível na raíz desse repositório.

# SCIAC-airflow
Para permitir a orquestração dos processos de extração, tratamento e carga dos dados (ETLs), optou-se por utilizar a ferramenta Open Source Apache Airflow, que, através de configuração via código em linguagem Python (configure as code), permite a customização dos processos e a construção de uma solução bastante robusta.
Esse módulo contém o código utilizado para construção da imagem docker "barbaravilela/sciac-airflow", disponível publicamente no DockerHub.
A seguir, uma explicação acerca do que fora implementado no protótipo, contido na imagem em questão.

* Configurações Apache Airflow - airflow.cfg:
No arquivo airflow.cfg foram definidos os parâmetros para sua execução, customizando-se os intervalos de processamento do seu processo de agendamento (scheduler) a fim de garantir condições apropriadas para a disponibilização do protótipo em ambiente de nuvem, sem uso excessivo de recursos computacionais.
Nele também estão definidas as credenciais de acesso, via SMTP, ao e-mail pucprojeto.sciac@hotmail.com, utilizado para envio de notificações relativas aos processos de ETL.

* DAGs:
O repositório dags é utilizado pelo Apache Airflow para acessar as DAGs (Directed Acyclic Graphs) configuradas. Elas são responsáveis por definir os parâmetros de execução das tarefas, sua ordem de execução e intervalos, dentre outros.
No protótipo em questão, construiu-se a dag 'dag_carga_centros_custos', que define os parâmetros para o processo de ETL relativo ao módulo de Centros de Custos do sistema.
Os ETLs relativos a esse módulo podem ser encontrados no caminho '/dags/etlScripts/centrosDeCustos/'.
Após execução das tarefas relativas ao módulo, a DAG envia e-mails de notificação, informando o status dos processos.

* ETLs do Módulo de Centros de Custos:
Esse módulo, construído para fins de prototipagem, visando estritamente a apresentação da arquitetura proposta, suas integrações com os diferentes sistemas e componentes internos, sugere o processo de ETL relativo ao conceito de Centros de Custos do SCIAC.
Para tal, foram construídas três tarefas:
- busca_centros_custos: Acessa uma APIFake, que simula o funcionamento do Sistema da Estrutura Organizacional do Município, de onde se obtém as informações relativas aos órgãos que compõem a instituição, armazenando os dados coletados em um arquivo temporário, a ser utilizado pela proxima tarefa;
- atualiza_centros_custos:   Obtém os centros de custos armazenados previamente na base de dados do SCIAC, contida no banco noSQL de grafos, neo4j (também disponível em ambiente de núvem), e compara com os dados obtidos pela tarefa anterior, atualizando os dados do SCIAC e salvando tais alterações no arquivo temporário;
- carrega_centros_custos: Carrega os dados do arquivo temporário, agora atualizados, na base de dados do SCIAC.

# SCIAC-APIFake
Contém o código, em node.js, da API Fake (dados mocados) que simula um serviço de um sistema externo, responsável pela estrutura organizacional do município.

 # Banco de Dados - Neo4j
Para atender às particularidades do SCIAC, propõe-se o uso de um banco de dados noSQL, orientado a grafos, o Neo4j.
Trata-se de um software Open Source, que permite grande agilidade nos processos de análises, além de tornar menos complexo o processo de modelagem e evoluções do sistema.

 # Acesso ao protótipo
Para acessar os componentes rodando em ambiente de nuvem, acesse os links abaixo:

* sciac-airflow: https://airflow.azurewebsites.net/
* sciac-APIFake: https://sciac-api-fake.azurewebsites.net/
* E-mail de notificações: https://outlook.live.com
* Banco de dados Neo4j: neo4j+s://1258ca96.databases.neo4j.io

As credenciais de acesso necessárias para testar a aplicação encontra-se no arquivo 'secret.txt'
Obs.: Os serviços estarão disponíveis apenas durante o período de avaliação do projeto.

 # Considerações finais
 O SCIAC é um sistema real, já em produção em um órgão do executivo municipal brasileiro, contudo, apresenta inúmeros desafios para sua continuidade, tais como: tecnologias já obsoletas, falhas nos processos e grande acoplamento de código.
 A proposta em questão baseia-se na reconstrução da aplicação, utilizando de um ferramental tecnológico mais moderno e robusto, com base nas restrições arquiteturais e requisitos funcionais e não funcionais identificados.
 Para fins reais, toda aplicação deverá ser implantada na estrutura interna da organização, já existente, amenizando os custos com provedores de nuvem. 
