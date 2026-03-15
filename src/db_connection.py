import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
MYSQL_HOST =os.getenv("MYSQL_HOST")
MYSQL_PORT =os.getenv("MYSQL_PORT")
MYSQL_DB=os.getenv("MYSQL_DB")
MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_PASS=os.getenv("MYSQL_PASS")



def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=os.getenv("MYSQL_PORT"),
        database=os.getenv("MYSQL_DB"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASS")
    )