import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

secret_key = os.environ.get("SECRET_KEY")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
db_link_asy = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'
db_link = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
