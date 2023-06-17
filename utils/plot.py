import matplotlib.pyplot as plt

def comparison_plot():
    # Data for each setting
    settings = ['S1', 'S2', 'S3', 'S5']
    
    S1 = [126, 126.5, 126.2, 126.1]
    S2 = [126, 142.3, 252.2, 145.2]
    S3 = [92.5, 181.8, 259.7, 181]
    S5 = [126, 137.4, 326.4, 142.4]
    
    

    # Creating the bar graph
    x = range(len(settings))
    width = 0.2

    fig, ax = plt.subplots()
    erb = ax.bar(x, erb_times, width, label='ERB')
    sumo = ax.bar([i + width for i in x], sumo_times, width, label='SUMO')
    fls = ax.bar([i + 2 * width for i in x], fls_times, width, label='FLS')
    bls = ax.bar([i + 3 * width for i in x], bls_times, width, label='BLS')

    # Adding labels, title, and legend
    ax.set_xlabel('Settings')
    ax.set_ylabel('Time taken (sec)')
    ax.set_title('EV Time Taken for Different Strategies & Settings, 45% Traffic Distributions')
    ax.set_xticks([i + 1.5 * width for i in x])
    ax.set_xticklabels(settings)
    ax.legend()

    plt.show()
    
def main():
    comparison_plot()

if __name__ == '__main__':
    main()