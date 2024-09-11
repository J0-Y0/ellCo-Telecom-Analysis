import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


class Str_analyzer:
    # Assuming cleaned_data is a Pandas DataFrame and graph.plot_histograms() is a custom function
    def plot_histograms(data, columns):
        # Set up the figure
        fig, axes = plt.subplots(nrows=len(columns), figsize=(10, len(columns) * 3))

        # Loop through each column and plot the histogram
        for i, column in enumerate(columns):
            sns.histplot(data[column], bins=30, ax=axes[i])
            axes[i].set_title(f"Histogram of {column}")

        plt.tight_layout()
        return fig

    # Streamlit App
    st.title("Histogram Plotter")

    # Cleaned Data (assuming you have cleaned_data available)
    # cleaned_data = ...  # Your dataframe goes here

    # List of columns for histogram plotting
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

    # Plot the histograms using the custom function
    if st.button("Plot Histograms"):
        fig = plot_histograms(cleaned_data, columns)
        st.pyplot(fig)
