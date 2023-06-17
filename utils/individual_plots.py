import numpy as np
import matplotlib.pyplot as plt
def plot_a_graph(duration):
    # Data
    settings = ['S1', 'S2', 'S3', 'S5']

     # ERB BLS FLS SUMO
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

    fig, ax = plt.subplots()

    rects1 = ax.bar(x - 1.5*width, ERB, width, label='ERB')
    rects2 = ax.bar(x - 0.5*width, SUMO, width, label='SUMO')
    rects3 = ax.bar(x + 0.5*width, FLS, width, label='FLS')
    rects4 = ax.bar(x + 1.5*width, BLS, width, label='BLS')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('EV Traversal Time')
    ax.set_xlabel('Settings')
    ax.set_title(f'For Lane change; Veh_Duration {duration}sec, EV Duration - {EV_DURATION}sec')
    ax.set_xticks(x)
    ax.set_xticklabels(settings)
    ax.legend()

    # Auto-rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()

def main():
    veh_durations = [2, 5, 10]

    for duration in veh_durations:
        print(f"Plotting graph for duration {duration} sec")
        plot_a_graph(duration)

if __name__=='__main__':
    main()