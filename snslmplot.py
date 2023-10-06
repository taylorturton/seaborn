# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (you can replace this with your own dataset)
data = sns.load_dataset("tips")  # Load the "tips" dataset from Seaborn as an example

# Create a Seaborn lmplot
sns.lmplot(x="total_bill", y="tip", data=data, hue="time")

# Add labels and a title
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Scatter Plot with Regression Lines (Time of Day)")

# Show the plot
plt.show()
