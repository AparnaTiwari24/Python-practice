# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style and figure size for all plots
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load the dataset (Car details dataset from CarDekho)
df = pd.read_csv("C:\\Users\\Aparna Tiwari\\python trainnig\\CAR_DETAILS_FROM_CAR_DEKHO.csv")
# Display the first 5 rows of the dataset
print(df.head())

# ---------------------- Data Visualization ----------------------


# 1. Fuel type distribution (count of each category)
sns.countplot(x='fuel',hue='fuel', data=df,palette="Set2")
plt.title('Fuel Type Distribution')
print(plt.show())


# 2. Selling price distribution (Histogram with KDE curve)
sns.histplot(df['selling_price'],kde=True,bins=20,color='Skyblue')
plt.title('Selling Price Distribution')
plt.xlabel('Price (INR)')
print(plt.show())

# 3. Boxplot of selling price grouped by fuel type
sns.boxplot(x='fuel',hue='fuel',y='selling_price',data=df,palette='Set1')
plt.title('Price Distribution by Fuel Type')
print(plt.show())

# 4. Boxplot of selling price grouped by transmission type
sns.boxplot(x='transmission',hue='transmission',y='selling_price',data=df,palette='coolwarm')
plt.title('Price Distribution by Fuel Type')
print(plt.show())