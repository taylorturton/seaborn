# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (you can replace this with your own dataset)
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 7]

# Create a Seaborn line plot
sns.set(style="whitegrid")  # Set the style of the plot (optional)
sns.lineplot(x=x, y=y)

# Add labels and a title
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Line Plot Example")

# Show the plot
plt.show()
