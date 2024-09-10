import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


class Analyzer:

    def load_data(self, query, engine):
        if engine and query:
            df = pd.read_sql_query(query, engine)
        else:
            print("Failed to retrieve data.")
            df = pd.DataFrame()  # Return an empty DataFrame if loading fails
        return df

    def missing_values(self, df):
        missing_value = df.isnull().sum()
        missing_percentage = 100 * df.isnull().sum() / len(df)

        missing = pd.concat([missing_value, missing_percentage], axis=1)
        missing.columns = ["Missing Value", "Percentage"]
        missing = missing.sort_values(by="Missing Value", ascending=False)
        missing = missing.round(2)
        return missing

    def drop_missing_values(self, df):
        missing = self.missing_values(df)
        high_missing_cols = missing[missing["Percentage"] > 50].index
        df.drop(columns=high_missing_cols, inplace=True)
        return df

    def fill_missing_values(self, df, fill_threshold=50, fill_value="mean"):

        missing = self.missing_values(df)

        # Identify columns to fill (excluding identifiers)
        cols_to_fill = missing[
            (missing["Percentage"] >= 10) & (missing["Percentage"] <= fill_threshold)
        ].index

        # Exclude identifier columns
        identifier_cols = ["bearer id"]
        cols_to_fill = [col for col in cols_to_fill if col not in identifier_cols]

        if fill_value == "mean":
            df[cols_to_fill] = df[cols_to_fill].fillna(
                df[cols_to_fill].mean(numeric_only=True)
            )
        elif fill_value == "median":
            df[cols_to_fill] = df[cols_to_fill].fillna(
                df[cols_to_fill].median(numeric_only=True)
            )
        elif fill_value == "placeholder":
            df[cols_to_fill] = df[cols_to_fill].fillna(
                "Unknown"
            )  # Example placeholder; adjust as needed
        else:
            raise ValueError(
                "Invalid fill_value. Choose from 'mean', 'median', or 'placeholder'."
            )

        return df

    def handle_missing_values(self, df):
        df = self.drop_missing_values(df)
        df = self.fill_missing_values(df)
        return df

    def keep_columns_with_minimal_missing_data(self, df, threshold=50):
        missing = self.missing_values(df)

        # Identify columns to keep (excluding identifiers)
        identifier_cols = ["bearer id"]
        columns_to_keep = missing[missing["Percentage"] <= threshold].index
        columns_to_keep = [col for col in columns_to_keep if col not in identifier_cols]
        df = df[columns_to_keep]

        return df

    def outliers(self, df, threshold=3):
        # Calculate Z-scores for numeric columns only
        numeric_df = df.select_dtypes(include=[float, int])
        z_scores = stats.zscore(numeric_df)

        # Identify outliers
        outliers = abs(z_scores) > threshold
        outlier_indices = df.index[outliers.any(axis=1)]
        return outlier_indices

    def handle_outliers(self, df):
        outlier_indices = self.outliers(df)
        df = df.drop(index=outlier_indices)
        return df

    def aggregate_user_data(self, df):
        # Define the columns to aggregate
        columns_to_aggregate = {
            "Bearer Id": "count",  # Number of xDR sessions
            "Dur. (ms)": "sum",  # Total session duration in ms
            "Total DL (Bytes)": "sum",  # Total download data in Bytes
            "Total UL (Bytes)": "sum",  # Total upload data in Bytes
            "Social Media DL (Bytes)": "sum",
            "Social Media UL (Bytes)": "sum",
            "Google DL (Bytes)": "sum",
            "Google UL (Bytes)": "sum",
            "Email DL (Bytes)": "sum",
            "Email UL (Bytes)": "sum",
            "Youtube DL (Bytes)": "sum",
            "Youtube UL (Bytes)": "sum",
            "Netflix DL (Bytes)": "sum",
            "Netflix UL (Bytes)": "sum",
            "Gaming DL (Bytes)": "sum",
            "Gaming UL (Bytes)": "sum",
            "Other DL (Bytes)": "sum",
            "Other UL (Bytes)": "sum",
        }

        # Group by user (assuming 'bearer id' is the user identifier)
        aggregated_data = df.groupby("MSISDN/Number").agg(columns_to_aggregate)

        # Rename columns for clarity
        aggregated_data.columns = [
            "Number of xDR Sessions",
            "Total Session Duration (ms)",
            "Total Download (DL) Data (Bytes)",
            "Total Upload (UL) Data (Bytes)",
            "Social Media DL (Bytes)",
            "Social Media UL (Bytes)",
            "Google DL (Bytes)",
            "Google UL (Bytes)",
            "Email DL (Bytes)",
            "Email UL (Bytes)",
            "YouTube DL (Bytes)",
            "YouTube UL (Bytes)",
            "Netflix DL (Bytes)",
            "Netflix UL (Bytes)",
            "Gaming DL (Bytes)",
            "Gaming UL (Bytes)",
            "Other DL (Bytes)",
            "Other UL (Bytes)",
        ]

        return aggregated_data

    def total_application_data(self, df):
        df["Total Social Media Data"] = (
            df["Social Media DL (Bytes)"] + df["Social Media UL (Bytes)"]
        )
        df["Total Google Data"] = df["Google DL (Bytes)"] + df["Google UL (Bytes)"]
        df["Total Email Data"] = df["Email DL (Bytes)"] + df["Email UL (Bytes)"]
        df["Total YouTube Data"] = df["Youtube DL (Bytes)"] + df["Youtube UL (Bytes)"]
        df["Total Netflix Data"] = df["Netflix DL (Bytes)"] + df["Netflix UL (Bytes)"]
        df["Total Gaming Data"] = df["Gaming DL (Bytes)"] + df["Gaming UL (Bytes)"]
        df["Total Other Data"] = df["Other DL (Bytes)"] + df["Other UL (Bytes)"]

        return df

    def compute_correlations(self, df):
        # Define columns for correlation
        columns = [
            "Total Social Media Data",
            "Total Google Data",
            "Total Email Data",
            "Total YouTube Data",
            "Total Netflix Data",
            "Total Gaming Data",
            "Total Other Data",
            "Total DL (Bytes)",
            "Total UL (Bytes)",
        ]

        df = self.total_application_data(df)
        # Select relevant columns
        data = df[columns]
        # Compute the correlation matrix
        correlation_matrix = data.corr()

        return correlation_matrix

    def cluster(self, df, colum, k):
        # Step 1: Normalize the 'count' column
        scaler = MinMaxScaler()
        df["normalized_count"] = scaler.fit_transform(df[[colum]])
        # Step 2: Apply K-means clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        df["engagement_cluster"] = kmeans.fit_predict(df[["normalized_count"]])
        return df

    def user_traffic_per_apk(self, df):
        df = self.total_application_data(df)
        user_traffic = (
            df.groupby("MSISDN/Number")
            .agg(
                {
                    "Total Google Data": "sum",
                    "Total Email Data": "sum",
                    "Total YouTube Data": "sum",
                    "Total Netflix Data": "sum",
                    "Total Gaming Data": "sum",
                    "Total Other Data": "sum",
                }
            )
            .reset_index()
        )
        return user_traffic
