#!/bin/bash

# Executa as migrações do Alembic
alembic upgrade head

# Inicia o servidor FastAPI com Uvicorn
uvicorn main:app --host 0.0.0.0 --port 80
