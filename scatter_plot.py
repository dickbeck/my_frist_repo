#This code uses Seaborn's built-in dataset on penguins and
#plots a scatter plot of bill length vs. bill depth,
#with different species color-coded.

import seaborn as sns
import matplotlib.pyplot as plt

# Sample data

data = sns.load_dataset('penguins')

# Create a scatter plot
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=data)

# Add labels and title
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.title('Penguin Bill Measurements')

# Display the plot
plt.show()
