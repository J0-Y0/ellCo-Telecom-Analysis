import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns


class Graph:

    def plot_histograms(self, df, variables):
        num_vars = len(variables)
        cols = 3  # Number of columns in the grid
        rows = (num_vars + cols - 1) // cols  # Compute the number of rows needed

        fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))

        # Flatten the axes array for easy iteration
        axes = axes.flatten()

        for i, var in enumerate(variables):
            axes[i].hist(df[var].dropna(), bins=30, edgecolor="black")
            axes[i].set_title(f"Histogram of {var}")
            axes[i].set_xlabel(var)
            axes[i].set_ylabel("Frequency")
            axes[i].grid(True)

        # Hide any unused subplots
        for j in range(i + 1, len(axes)):
            axes[j].axis("off")

        plt.tight_layout()
        plt.show()

    def plot_correlation_heatmap(self, correlation_matrix):
        plt.figure(figsize=(12, 10))
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
            center=0,
            fmt=".2f",
            linewidths=0.5,
            linecolor="black",
        )
        plt.title("Correlation Matrix Heatmap")
        plt.show()
