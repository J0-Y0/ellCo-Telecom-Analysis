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

    def plot_engagement_cluster(self, df):
        # Set up the visualization style
        # sns.set(style="whitegrid")

        # Step 5: Visualizing the clusters
        fig, axes = plt.subplots(2, 3, figsize=(14, 10))

        # Min Engagement
        sns.barplot(x="Cluster", y="Min Engagement", data=df, ax=axes[0, 0])
        axes[0, 0].set_title("Min Engagement per Cluster")

        # Max Engagement
        sns.barplot(x="Cluster", y="Max Engagement", data=df, ax=axes[0, 1])
        axes[0, 1].set_title("Max Engagement per Cluster")

        # Average Engagement
        sns.barplot(x="Cluster", y="Average Engagement", data=df, ax=axes[0, 2])
        axes[0, 2].set_title("Average Engagement per Cluster")

        # Total Engagement
        sns.barplot(x="Cluster", y="Total Engagement", data=df, ax=axes[1, 0])
        axes[1, 0].set_title("Total Engagement per Cluster")
        # Total Customer gement
        sns.barplot(x="Cluster", y="Number of Customer", data=df, ax=axes[1, 2])
        axes[1, 2].set_title("Customer per Cluster")

        # Adjust layout for better viewing
        plt.tight_layout()
        plt.show()

    def plot_most_used_apk(self, df):
        # Step 3: Aggregate total traffic for each application across all users
        total_traffic_per_app = {
            "Google": df["Total Google Data"].sum(),
            "Email": df["Total Email Data"].sum(),
            "YouTube": df["Total YouTube Data"].sum(),
            "Netflix": df["Total Netflix Data"].sum(),
            "Gaming": df["Total Gaming Data"].sum(),
            "Other": df["Total Other Data"].sum(),
        }

        # Convert to DataFrame for easier plotting
        traffic_df = pd.DataFrame(
            list(total_traffic_per_app.items()),
            columns=["Application", "Total_Traffic"],
        )

        # Identify the top 3 most used applications
        top_3_apps = traffic_df.nlargest(3, "Total_Traffic")

        fig, axes = plt.subplots(1, 2, figsize=(14, 6))

        # Bar plot for total traffic
        sns.barplot(
            x="Application",
            y="Total_Traffic",
            data=top_3_apps,
            hue="Application",
            palette="viridis",  # Use palette directly if not using hue
            ax=axes[0],
        )
        axes[0].set_title("Top 3 Most Used Applications by Total Traffic")
        axes[0].set_xlabel("Application")
        axes[0].set_ylabel("Total Traffic (Bytes)")

        # Pie chart for traffic distribution
        axes[1].pie(
            top_3_apps["Total_Traffic"],
            labels=top_3_apps["Application"],
            autopct="%1.1f%%",
            colors=sns.color_palette("viridis", 3),
            startangle=140,
        )
        axes[1].set_title("Traffic Distribution of Top 3 Most Used Applications")

        plt.tight_layout()
        plt.show()
