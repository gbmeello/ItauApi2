FROM python:3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

ENV an_env_var=$A_VARIABLE
ENV PG_USER=$PG_USER
ENV PG_PASSWORD=$PG_PASSWORD
ENV PG_DB=$PG_DB
ENV PGADMIN_DEFAULT_EMAIL=$PGADMIN_DEFAULT_EMAIL
ENV PGADMIN_DEFAULT_PASSWORD=$PGADMIN_DEFAULT_PASSWORD


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /code/app


CMD ["alembic", "upgrade", "head","fastapi", "run", "app/main.py", "--port", "80"]