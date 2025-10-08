import os
import mysql.connector
from dotenv import load_dotenv

# variables de entorno
load_dotenv()
HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("USER")
PASS = os.getenv("PASS")
PORT = os.getenv("PORT")


class DBConnection:

    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(
                host=HOST, database=DB_NAME, user=USER, password=PASS, port=PORT
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
