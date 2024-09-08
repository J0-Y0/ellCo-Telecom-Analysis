import pandas as pd
import matplotlib.pyplot as plt


class Analyzer:

    def load_data(self, query, engine):
        if engine and query:
            # Load data into a DataFrame using the SQLAlchemy engine
            df = pd.read_sql_query(query, engine)
        else:
            print("Failed to retrieve data.")
        return df

    def missing_values(self, df):
        missing_value = df.isnull().sum()
        missing_percentage = 100 * df.isnull().sum() / len(df)
        missing = pd.concat([missing_value, missing_percentage], axis=1)
        missing = missing.rename(columns={0: "Missing Value", 1: "Percentage"})
        missing = missing.sort_values(by="Missing Value", ascending=False)

        return missing
