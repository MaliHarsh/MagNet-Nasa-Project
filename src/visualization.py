# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

# MagNet-Nasa-Project
def show_enhanced_visualization(data, save_dir="data/plots/"):
    """
    Function to show enhanced visualizations for the given dataset.
    Includes line plots, histograms, and scatter plots.
    Saves the plots to the specified directory.
    """
    # Set the style for the plots
    sns.set(style="whitegrid")
    
    # Ensure the save directory exists
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    
    # Create a large figure with multiple subplots
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 18), dpi=100)
    colors = sns.color_palette("Set2", len(data.columns))  # Use Seaborn's color palette

    # Plot 1: Line plots of each feature
    for i, key in enumerate(data.columns[:3]):  # First 3 features as line plots
        t_data = data[key]
        ax = t_data.plot(
            ax=axes[i, 0],
            title=f"Line Plot - {key.capitalize()}",
            color=colors[i],
            lw=2
        )
        ax.set_xlabel("Index")
        ax.set_ylabel(key.capitalize())
        ax.axvline(t_data.idxmax(), color='k', linestyle='--', lw=1, label=f"Max: {t_data.max():.2f}")
        ax.axvline(t_data.idxmin(), color='grey', linestyle='--', lw=1, label=f"Min: {t_data.min():.2f}")
        ax.legend(loc='best')

    # Plot 2: Histograms of the features
    for i, key in enumerate(data.columns[:3]):  # First 3 features as histograms
        t_data = data[key]
        sns.histplot(t_data, ax=axes[i, 1], color=colors[i], kde=True)
        axes[i, 1].set_title(f"Histogram - {key.capitalize()}")
        axes[i, 1].set_xlabel(key.capitalize())
        axes[i, 1].set_ylabel("Frequency")

    # Plot 3: Scatter plots to show correlations
    for i, key in enumerate(data.columns[1:4]):  # Pairwise scatter plot of second and third columns
        x_data = data[data.columns[0]]
        y_data = data[key]
        sns.scatterplot(x=x_data, y=y_data, ax=axes[i, 2], color=colors[i], s=50)
        axes[i, 2].set_title(f"Scatter Plot: {data.columns[0].capitalize()} vs {key.capitalize()}")
        axes[i, 2].set_xlabel(data.columns[0].capitalize())
        axes[i, 2].set_ylabel(key.capitalize())

    # Adjust layout to avoid overlap
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    plt.tight_layout()

    # Save the figure to the specified directory
    plot_file = save_path / "enhanced_visualization.png"
    plt.savefig(plot_file)
    logging.info(f"Plots saved to {plot_file}")

    # Close the plot to free up memory
    plt.close(fig)

# Example call to function with sample data
# Assuming `data` is a pandas DataFrame
# show_enhanced_visualization(data)
