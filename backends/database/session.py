from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from backends.core.config import settings

from sqlalchemy.ext.declarative import declarative_base

import pymysql
pymysql.install_as_MySQLdb()

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = settings.DB_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()
        

if __name__ == "__main__":
    
    from sqlalchemy import text
    
    connection = engine.connect()
    
    query = "SELECT * FROM task"
    result = connection.execution_options(stream_result=True).execute(
        text(query)
    )
    for row in result:
        print(row)    
    
    connection.close()