# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (fictional football data)
data = {
    'Team': ['Team A', 'Team B', 'Team C', 'Team D'],
    'Average Goals Scored': [2.5, 1.8, 3.2, 2.1]
}

# Create a Seaborn barplot
sns.set(style="whitegrid")  # Set the style of the plot (optional)
sns.barplot(x='Team', y='Average Goals Scored', data=data)

# Add labels and a title
plt.xlabel("Football Team")
plt.ylabel("Average Goals Scored")
plt.title("Average Goals Scored by Football Team")

# Show the plot
plt.show()
