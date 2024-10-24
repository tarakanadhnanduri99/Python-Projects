import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\titanic-2.csv")

# 1. Bar Chart: Survival Count by Passenger Class
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', hue='Survived', data=data, palette='viridis')
plt.title('Survival Count by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(['Not Survived', 'Survived'])
plt.show()

# 2. Age Distribution by Survival Status
plt.figure(figsize=(8, 6))
sns.histplot(data=data, x='Age', hue='Survived', kde=True, palette='coolwarm', bins=30)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# 3. Boxplot: Fare Distribution by Passenger Class
plt.figure(figsize=(8, 6))
sns.boxplot(x='Pclass', y='Fare', data=data, palette='Set2')
plt.title('Fare Distribution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

# 4. Heatmap: Correlation Matrix (Exclude non-numeric columns)
numeric_data = data.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heatmap of Correlations')
plt.show()

# 5. Scatter Plot: Age vs Fare for Survivors
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=data, palette='coolwarm')
plt.title('Scatter Plot of Age vs Fare (Survivors)')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
