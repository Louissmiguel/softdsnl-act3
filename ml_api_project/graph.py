import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('my_dataset.csv')  # Make sure this matches your CSV filename

# Show a scatterplot of tail length vs ear size, colored by breed
sns.scatterplot(data=data, x='tail_length', y='ear_size', hue='breed', s=100)

plt.title('Dog Breeds by Tail Length and Ear Size')
plt.xlabel('Tail Length')
plt.ylabel('Ear Size')
plt.legend(title='Breed')
plt.grid(True)
plt.tight_layout()
plt.show()
