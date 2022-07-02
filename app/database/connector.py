import yaml

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("./resources/database.yml", "r") as stream:
    try:
        db_config = yaml.safe_load(stream)
        db_con_url = db_config['db']['url']
        Engine = create_engine(db_con_url)
        SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=Engine)
        Base = declarative_base()
    except yaml.YAMLError as e:
        print("Error loading database configuration:", e)

