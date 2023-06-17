import matplotlib.pyplot as plt
import numpy as np

# Data from the table
strategies = ['ERB', 'BLS', 'FLS', 'SUMO']
x_values = ['ERB', 'BLS', 'FLS', 'SUMO']
y_values_500 = np.array([32, 40.7, 66.5, 47.7])
y_values_2000 = np.array([126, 142.7, 330.2, 145.4])
y_values_4000 = np.array([250.0, 276.8, 682.6, 283.1])

# Generate random colors
colors = np.random.rand(len(strategies), 3)

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
fig.suptitle('Road Lengths for Different Strategies in S5')

# Plot data for 500
axs[0].bar(x_values, y_values_500, color=colors)
axs[0].set_title('Road Lengths at 500m')
axs[0].set_xlabel('Strategy')
axs[0].set_ylabel('Value')

# Plot data for 2000
axs[1].bar(x_values, y_values_2000, color=colors)
axs[1].set_title('Road Lengths at 2000m')
axs[1].set_xlabel('Strategy')
axs[1].set_ylabel('Value')

# Plot data for 4000
axs[2].bar(x_values, y_values_4000, color=colors)
axs[2].set_title('Road Lengths at 4000m')
axs[2].set_xlabel('Strategy')
axs[2].set_ylabel('Value')

plt.tight_layout()
plt.show()
