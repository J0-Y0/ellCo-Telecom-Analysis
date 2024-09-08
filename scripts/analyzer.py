import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


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
        missing = missing.round(2)
        # df_rounded_specific = df.round({'A': 2

        return missing

    # handles missing values by dropping columns with more than 50% missing data.
    def handle_missing_values(self, df):
        missing = self.missing_values(df)
        high_missing_cols = missing[missing["Percentage"] > 50].index
        # Drop columns with high percentage of missing values

        df.drop(columns=high_missing_cols, inplace=True)
        return df

    # - strategy: The strategy to use for filling missing values; options are 'mean', 'median', or 'placeholder'
    def fill_missing_values(self, df, strategy="mean"):
        if strategy == "mean":
            df.fillna(df.mean(numeric_only=True), inplace=True)
        elif strategy == "median":
            df.fillna(df.median(numeric_only=True), inplace=True)
        elif strategy == "placeholder":
            df.fillna("Unknown", inplace=True)  # Example placeholder; adjust as needed
        else:
            raise ValueError(
                "Invalid strategy. Choose from 'mean', 'median', or 'placeholder'."
            )

        return df

    def outliers(self, df, threshold=3):
        # Calculate Z-scores
        z_scores = stats.zscore(df)

        # Identify outliers
        outliers = abs(z_scores) > threshold
        outlier_indices = df.index[outliers.any(axis=1)]
        return outlier_indices
