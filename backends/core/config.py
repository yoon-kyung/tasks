import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./backends/task.env')

class Settings:
    
    # database
    DB_USER_NAME: str = os.getenv("DB_USER_NAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_SERVER: str = os.getenv("DB_SERVER")
    DB_PORT: str = os.getenv("DB_PORT", 5432)
    DB_DBNAME: str = os.getenv("DB_DBNAME", "synthea_1000")
    DB_URL = f"mysql+mysqldb://{DB_USER_NAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_DBNAME}"


settings = Settings()