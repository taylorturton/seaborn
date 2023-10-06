# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (you can replace this with your own dataset)
data = sns.load_dataset("iris")  # Load the "iris" dataset from Seaborn as an example

# Create a Seaborn jointplot
sns.set(style="whitegrid")  # Set the style of the plot (optional)
g = sns.jointplot(x="sepal_length", y="sepal_width", data=data, kind="scatter")

# Add labels and a title
g.set_axis_labels("Sepal Length (cm)", "Sepal Width (cm)")
g.fig.suptitle("Joint Plot of Sepal Length vs. Sepal Width", y=0.95)  # Adjust title position

# Show the plot
plt.tight_layout()  # Automatically adjust subplot parameters
plt.show()
