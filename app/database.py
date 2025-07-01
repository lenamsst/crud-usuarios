from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Pega a string de conexão com o banco
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria a engine do SQLAlchemy para conectar ao banco
engine = create_engine(DATABASE_URL)

# Cria a sessão que será usada para executar comandos no banco
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Cria a base para os modelos (tabelas)
Base = declarative_base()
