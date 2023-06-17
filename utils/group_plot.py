import numpy as np
import matplotlib.pyplot as plt

def plot_a_graph(duration, ax):
    # Data
    settings = ['S1', 'S2', 'S3', 'S5']
    EV_DURATION = 10
    if duration == 2:
        S1 = [126, 126.2, 126.1, 126.1]
        S2 = [126, 137.9, 154.2, 146.1]
        S3 = [94.9, 162.1, 148.6, 191.6]
        S5 = [126, 144.2, 326, 146.1]

    elif duration == 5:
        S1 = [126, 126.4, 126.1, 126.1]
        S2 = [126, 137.2, 149.6, 146.1]
        S3 = [94.9, 172.6, 139.1, 191.6]
        S5 = [126, 144.2, 326, 146.1]

    elif duration == 10:
        S1 = [126, 126.2, 126, 126.1]
        S2 = [126, 136.8, 143.5, 146.1]
        S3 = [94.9, 192.6, 135.3, 191.6]
        S5 = [126, 144.2, 326, 146.1]

    ERB = [S1[0], S2[0], S3[0], S5[0]]
    SUMO = [S1[3], S2[3], S3[3], S5[3]]
    FLS = [S1[2], S2[2], S3[2], S5[2]]
    BLS = [S1[1], S2[1], S3[1], S5[1]]

    # Plotting
    width = 0.2
    x = np.arange(len(settings))

    rects1 = ax.bar(x - 1.5*width, ERB, width, label='ERB')
    rects2 = ax.bar(x - 0.5*width, SUMO, width, label='SUMO')
    rects3 = ax.bar(x + 0.5*width, FLS, width, label='FLS')
    rects4 = ax.bar(x + 1.5*width, BLS, width, label='BLS')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('EV Traversal Time')
    ax.set_xlabel('Settings')
    ax.set_title(f'EV-{EV_DURATION} & VD-{duration}')
    ax.set_xticks(x)
    ax.set_xticklabels(settings)
    ax.legend()

    # Enable grid
    #ax.grid(True, color='lightgray', alpha=0.5)

    # Auto-rotate x-axis labels for better readability
    plt.xticks(rotation=45)



def main():
    durations = [2, 5, 10]
    # Create a single figure for all the plots
    fig, axs = plt.subplots(1, len(durations), figsize=(15, 5))
    
    for i, duration in enumerate(durations):
        ax = axs[i]
        plot_a_graph(duration, ax)

    # Adjust spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()

if __name__=='__main__':
    main()
