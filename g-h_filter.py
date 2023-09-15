import matplotlib.pyplot as plt
import numpy as np

def g_h_filter(data, x0, dx, g, h, dt=1.):
    x_est = x0
    results = []
    for z in data:
        # prediction step
        x_pred = x_est + (dx * dt)
        dx = dx

        # update step
        residual = z - x_pred
        dx = dx + h * (residual) / dt
        x_est = x_pred + g * residual
        results.append(x_est)
    return np.array(results)

# Simulated data for weights
weights = np.array([158.0, 164.2, 160.3, 159.9, 162.1, 164.6, 169.6, 167.4, 166.4, 171.0, 171.2, 172.6])

# Actual weight plot
plt.plot(range(len(weights)), weights, label='Measured State', marker='o')

# Apply the g-h filter to the data
filtered_data = g_h_filter(data=weights, x0=160., dx=1., g=6./10, h=2./3, dt=1.)

# Filtered weight plot
plt.plot(range(len(filtered_data)), filtered_data, label='Filtered State', linestyle='--', marker='x')

start_value, end_value = 160, 172
num_increments = 12

# Generate evenly spaced x-values
x_values = np.arange(num_increments)

# Corresponding y-values (you can modify this as needed)
y_values = np.linspace(start_value, end_value, num=num_increments)

# Create the line plot
plt.plot(x_values, y_values, label='Actual State', linestyle='-')

# Add labels and legend
plt.xlabel('Time Step')
plt.ylabel('State')
plt.title('Figure 1: Comparison of Measured and Filter state against actual state')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

print("Actual Weights:", weights)
print("Filtered Weights:", filtered_data)
