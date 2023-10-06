# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (fictional student exam scores)
data = {
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'History', 'History', 'History'],
    'Score': [85, 92, 78, 70, 65, 80, 88, 75, 90]
}

# Create a Seaborn violin plot
sns.set(style="whitegrid")  # Set the style of the plot (optional)
sns.violinplot(x='Subject', y='Score', data=data, palette='Set3')  # Use the Set3 color palette

# Add labels and a title
plt.xlabel("Subject")
plt.ylabel("Exam Score")
plt.title("Distribution of Exam Scores by Subject (Violin Plot)")

# Show the plot
plt.show()
