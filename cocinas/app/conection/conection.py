import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

current_dir = os.path.dirname(__file__)
credentials_path = os.path.join(current_dir, 'credentials.json')

with open(credentials_path, 'r') as file:
    config = json.load(file)    

db_password = config.get('password') 
db_username = config.get('username') 
db_host = config.get('host') 
db_port = config.get('port') 
db_database = config.get('database') 


database_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}"

engine = create_engine(database_url, echo=True)

sessionBD = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()
