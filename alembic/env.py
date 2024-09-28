# alembic/env.py

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Importar seus modelos para que o Alembic possa detectá-los
from database.connection import Base  # Certifique-se de que está importando a Base correta
from models.client_models import Client  # Importar os modelos

# Configurações
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata  # Associar a metadata da Base

# Funções padrão do Alembic (run_migrations_online etc.)
