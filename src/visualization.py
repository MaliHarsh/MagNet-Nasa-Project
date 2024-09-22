# MagNet-Nasa-Project
def show_enhanced_visualization(data):
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15), dpi=80)
    colors = ['b', 'g', 'r', 'c', 'm', 'y']  # Define a color palette for variety

    for i, key in enumerate(data.columns):
        t_data = data[key]
        ax = t_data.plot(
            ax=axes[i // 2, i % 2],
            title=f"{key.capitalize()}",
            color=colors[i],
            rot=25,
            lw=2  # Set line width for better visibility
        )
        ax.set_xlabel("Index")  # Add x-label for better understanding
        ax.set_ylabel(key.capitalize())  # Add y-label corresponding to the data type

        # Highlight the min and max points on each plot
        ax.axvline(t_data.idxmax(), color='k', linestyle='--', lw=1, label=f"Max: {t_data.max():.2f}")
        ax.axvline(t_data.idxmin(), color='grey', linestyle='--', lw=1, label=f"Min: {t_data.min():.2f}")
        ax.legend(loc='best')  # Display a legend for clarity

    fig.subplots_adjust(hspace=0.8)
    plt.tight_layout()
