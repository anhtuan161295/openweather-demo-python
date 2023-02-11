from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker
from config import config

dbConfig = config.get_settings()

SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(
    dbConfig.database_username,
    dbConfig.database_password,
    dbConfig.database_url,
    dbConfig.database_port,
    dbConfig.database_name
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()


def get_session():
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()


def get_base():
    return base
