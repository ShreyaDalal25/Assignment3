import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Display the first few rows of the dataset
print(iris.head())

# Pairplot for overall distribution
sns.pairplot(iris, hue="species")
plt.title("Pairplot of Iris Dataset")
plt.show()

# Boxplot for each feature across species
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris, orient="h")
plt.title("Boxplot of Iris Dataset")
plt.show()

# Violin plot for each feature across species
plt.figure(figsize=(10, 6))
sns.violinplot(x="species", y="sepal_length", data=iris)
plt.title("Violin Plot of Sepal Length Across Species")
plt.show()
