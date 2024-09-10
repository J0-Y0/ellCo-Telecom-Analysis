import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


class DbConnection:
    def __init__(self):
        """Initialize the database connection parameters and create the engine."""
        self.conn_params = {
            "dbname": os.getenv("DBNAME"),
            "user": os.getenv("DBUSER"),
            "password": os.getenv("DBPASSWORD"),
            "host": os.getenv("DBHOST"),
            "port": os.getenv("DBPORT"),
        }
        try:
            self.engine = self.create_engine()
            print("DB connection engine created successfully.")
        except Exception as e:
            print(f"Failed to create DB connection engine: {e}")
            self.engine = None

    def create_engine(self):
        """Create and return an SQLAlchemy engine."""
        DATABASE_URI = (
            f"postgresql+psycopg2://"
            f"{self.conn_params['user']}:{self.conn_params['password']}@"
            f"{self.conn_params['host']}:{self.conn_params['port']}/"
            f"{self.conn_params['dbname']}"
        )
        try:
            engine = create_engine(DATABASE_URI)
            return engine
        except Exception as e:
            print(f"Failed to create SQLAlchemy engine: {e}")
            return None

    def get_engine(self):
        """Return the SQLAlchemy engine."""
        if self.engine:
            return self.engine
        else:
            raise ConnectionError("SQLAlchemy engine is not available.")

    def select_all_query(self):
        """Return SQL query to fetch all rows from the xdr_data table."""
        try:
            query = "SELECT * FROM public.xdr_data;"
            return query
        except Exception as e:
            print(f"Failed to fetch query: {e}")
            return None

    def select_aggregate_query(self, agg_column, alias, function):
        """
        Return SQL query to aggregate xdr_data table.

        Parameters:
        column (str): Column to group by.
        function (str): Aggregation function (e.g., 'SUM', 'AVG').
        agg_column (str): Column to apply the aggregation function to.

        Returns:
        str: SQL query string.
        """
        try:
            query = f"""
            SELECT {agg_column} {alias} , {function}(*) 
            FROM public.xdr_data
            WHERE {agg_column} is  Not Null
            GROUP BY {agg_column}
            ORDER BY {function}({agg_column})  desc;
            """
            return query
        except Exception as e:
            print(f"Failed to fetch query: {e}")
            return None
