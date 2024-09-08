import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DbConnection:
    def __init__(self):
        self.conn_params = {
            "dbname": os.getenv("dbname"),
            "user": os.getenv("user"),
            "password": os.getenv("password"),
            "host": os.getenv("host"),
            "port": os.getenv("port"),
        }

    def get_connection(self):
        return psycopg2.connect(**self.conn_params)

    def get_all_rows(self):
        return "SELECT * FROM public.xdr_data"
