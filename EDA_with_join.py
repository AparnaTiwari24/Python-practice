"""
EDA2.py

This script performs **Exploratory Data Analysis (EDA)** and feature engineering 
on an insurance dataset. It demonstrates:
- Reading datasets using pandas
- Data transformation (Box-Cox, Log transformation)
- Feature engineering (categorical grouping, derived features)
- Data visualization using seaborn & matplotlib
- Joining multiple datasets (students & courses) using different join types

Author: Aparna Tiwari
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the insurance dataset
df = pd.read_csv(r'C:\Users\Aparna Tiwari\python trainnig\Pandas\insurance.csv')
print(df.head(5))

# Plot histogram of charges with kernel density estimation (KDE)
sns.histplot(df['charges'], kde=True)
print(plt.show())

# Data Transformation: Box-Cox Transformation for 'bmi'
# Box-Cox requires all positive values, so we add 1 to avoid log(0)
from scipy.stats import boxcox
df['bmi_boxcox'], _ = boxcox(df['bmi'] + 1)

print(df.head())

# Log Transformation of charges (to reduce skewness in distribution)
import numpy as np
df['log_charges']= np.log1p(df['charges'])
sns.histplot(df['log_charges'], kde=True)
print(plt.show())

print(df.head())

# Feature Engineering
# Creating new columns from existing ones
# Example: Convert continuous variables into categorical groups

# Categorize BMI into underweight, normal, overweight, and obese
df['bmi_cat'] = pd.cut(df['bmi'], bins=[0,18.5,25,30,100], labels=['under','normal','over','obese'])

# Categorize age into groups: young, adult, mature, senior
df['age_group'] = pd.cut(df['age'], bins=[17, 30, 45, 60, 100],labels=['young', 'adult', 'mature', 'senior'])

# Create new feature: product of age with smoker status
# (age if smoker == 'yes', otherwise 0)
df['age_smoker'] = df['age'] * (df['smoker']== 'yes')


print(df.head())

# Visualization: Compare transformed features
sns.histplot(df['log_charges'], kde=True)
sns.histplot(df['bmi_boxcox'], kde=True)

# Boxplot: Charges vs BMI category
sns.boxplot(x ='bmi_cat', y = 'charges',data=df)
print(plt.show()) 

# Boxplot: Charges vs Smoker status
sns.boxplot(x='smoker', y ='charges',data=df)
print(plt.show())


# Working with Multiple Datasets
# Load students and courses datasets

df_students = pd.read_csv(r'C:\Users\Aparna Tiwari\python trainnig\Pandas\students.csv')
print(df_students.head())


df_courses = pd.read_csv(r'C:\Users\Aparna Tiwari\python trainnig\Pandas\courses.csv')
print(df_courses.head())  
                        
# JOINS in Pandas

# INNER JOIN: Only matching Course_ID in both datasets

inner_join = pd.merge(df_students, df_courses, on="Course_ID", how="inner")
print("INNER JOIN Result:")
print(inner_join, "\n")

# OUTER JOIN: All records from both datasets (NaN if no match)
outer_join = pd.merge(df_students, df_courses, on="Course_ID", how="outer")
print("OUTER JOIN Result:")
print(outer_join, "\n")

# LEFT JOIN: All records from students + matching courses
left_join = pd.merge(df_students, df_courses, on="Course_ID", how="left")
print("LEFT JOIN Result:")
print(left_join, "\n")

# RIGHT JOIN: All records from courses + matching students
right_join = pd.merge(df_students, df_courses, on="Course_ID", how="right")
print("RIGHT JOIN Result:")
print(right_join, "\n")