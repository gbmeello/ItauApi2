FROM python:3.9

WORKDIR /code

# Copia os requisitos e instala as dependências
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Definir variáveis de ambiente
ENV an_env_var=$A_VARIABLE
ENV PG_USER=$PG_USER
ENV PG_PASSWORD=$PG_PASSWORD
ENV PG_DB=$PG_DB
ENV PGADMIN_DEFAULT_EMAIL=$PGADMIN_DEFAULT_EMAIL
ENV PGADMIN_DEFAULT_PASSWORD=$PGADMIN_DEFAULT_PASSWORD
ENV ENVIRONMENT=$ENVIRONMENT

# Copia o código da aplicação
COPY . /code

# Copia o arquivo alembic.ini para o contêiner
COPY ./alembic /code/alembic
COPY ./alembic.ini /code/alembic.ini

# Copia o script de inicialização
COPY ./start.sh /code/start.sh
RUN chmod +x /code/start.sh

# Define o comando para rodar o script
CMD ["/code/start.sh"]
