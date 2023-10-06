# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (fictional tennis data)
data = {
    'Gender': ['Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Age': [28, 30, 25, 32, 27, 29, 26, 31, 28]
}

# Create a Seaborn boxplot
sns.set(style="whitegrid")  # Set the style of the plot (optional)
sns.boxplot(x='Gender', y='Age', data=data, palette='Set2')  # Use the Set2 color palette

# Add labels and a title
plt.xlabel("Gender")
plt.ylabel("Age")
plt.title("Distribution of Player Ages by Gender")

# Show the plot
plt.show()
