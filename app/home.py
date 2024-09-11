import os

# os.chdir("..")  # set the working directory one level up
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
)
from db_connection import DbConnection
from analyzer import Analyzer
from streamlit_script import Str_analyzer
import streamlit as str


db_connection = DbConnection()
analyzer = Analyzer()


engin = db_connection.get_engine()
query = db_connection.select_all_query()
data = analyzer.load_data(query, engin)

columns = [
    "Bearer Id",  # Number of xDR sessions
    "Dur. (ms)",  # Total session duration in ms
    "Total DL (Bytes)",  # Total download data in Bytes
    "Total UL (Bytes)",  # Total upload data in Bytes
    "Social Media DL (Bytes)",
    "Social Media UL (Bytes)",
    "Google DL (Bytes)",
    "Google UL (Bytes)",
    "Email DL (Bytes)",
    "Email UL (Bytes)",
    "Youtube DL (Bytes)",
    "Youtube UL (Bytes)",
    "Netflix DL (Bytes)",
    "Netflix UL (Bytes)",
    "Gaming DL (Bytes)",
    "Gaming UL (Bytes)",
    "Other DL (Bytes)",
    "Other UL (Bytes)",
]
cleaned_data = analyzer.handle_missing_values(data)
cleaned_data = analyzer.handle_outliers(cleaned_data)
if str.button("Plot Histograms"):
    fig = Str_analyzer.plot_histograms(cleaned_data, columns)
    str.pyplot(fig)
