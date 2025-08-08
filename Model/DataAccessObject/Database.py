import os
from dotenv import load_dotenv
import psycopg2

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv()  # Charger les variables depuis .env
            conn_str = (
                f"host={os.getenv('DB_HOST')} "
                f"port={os.getenv('DB_PORT')} "
                f"dbname={os.getenv('DB_NAME')} "
                f"user={os.getenv('DB_USER')} "
                f"password={os.getenv('DB_PASSWORD')}"
            )
            cls._instance = psycopg2.connect(conn_str)
        return cls._instance