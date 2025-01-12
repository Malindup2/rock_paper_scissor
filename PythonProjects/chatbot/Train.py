import matplotlib.pyplot as plt
import numpy as np

# Define the function (e.g., sine function)
x = np.linspace(0, 10, 100)  # Generate 100 points between 0 and 10
y = np.sin(x)  # Apply the sine function to the points

# Create the plot
plt.plot(x, y, label="Sine Wave")

# Add title and labels
plt.title("Plot of the Sine Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis (sin(x))")

# Add a legend
plt.legend()

# Display the plot
plt.show()
