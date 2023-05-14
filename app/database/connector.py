import os
import yaml

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("./resources/database.yml", "r") as stream:
    try:
        db_config = yaml.safe_load(stream)
        db_url: str = db_config['db']['url']
        db_url = db_url.replace('localhost', str(os.getenv('DATABASE_HOST') or "localhost"))
        Engine = create_engine(db_url)
        SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=Engine)
        Base = declarative_base()
    except yaml.YAMLError as e:
        print("Error loading database configuration:", e)
