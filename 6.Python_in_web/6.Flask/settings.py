import atexit
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind=engine)
atexit.register(lambda: engine.dispose())
Base.metadata.create_all(engine)
app = Flask('server')