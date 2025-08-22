import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Aparna Tiwari\python trainnig\Pandas\insurance.csv')
print(df.head(5))

sns.histplot(df['charges'], kde=True)
print(plt.show())
#sns.histplot(df['charges'], kde=True)
#print(sns.histplot())


from scipy.stats import boxcox
df['bmi_boxcox'], _ = boxcox(df['bmi'] + 1)

print(df.head())

import numpy as np
df['log_charges']= np.log1p(df['charges'])
sns.histplot(df['log_charges'], kde=True)
print(plt.show())

print(df.head())

## feature engineering means combining two columns and making one new column from them eg : height and weight it will give bmi
## and it we can do like if there is age in numerical from we can create a new column in caterogical data which will give young,elder


df['bmi_cat'] = pd.cut(df['bmi'], bins=[0,18.5,25,30,100], labels=['under','normal','over','obese'])
df['age_group'] = pd.cut(df['age'], bins=[17, 30, 45, 60, 100],labels=['young', 'adult', 'mature', 'senior'])
df['age_smoker'] = df['age'] * (df['smoker']== 'yes')


print(df.head())

sns.histplot(df['log_charges'], kde=True)
sns.histplot(df['bmi_boxcox'], kde=True)
sns.boxplot(x ='bmi_cat', y = 'charges',data=df)
print(plt.show()) 

sns.boxplot(x='smoker', y ='charges',data=df)
print(plt.show())


df_students = pd.read_csv(r'C:\Users\Aparna Tiwari\python trainnig\Pandas\students.csv')
print(df_students.head())


df_courses = pd.read_csv(r'C:\Users\Aparna Tiwari\python trainnig\Pandas\courses.csv')
print(df_courses.head())  
                        
# joins

inner_join = pd.merge(df_students, df_courses, on="Course_ID", how="inner")
print("INNER JOIN Result:")
print(inner_join, "\n")

outer_join = pd.merge(df_students, df_courses, on="Course_ID", how="outer")
print("OUTER JOIN Result:")
print(outer_join, "\n")

left_join = pd.merge(df_students, df_courses, on="Course_ID", how="left")
print("LEFT JOIN Result:")
print(left_join, "\n")

right_join = pd.merge(df_students, df_courses, on="Course_ID", how="right")
print("RIGHT JOIN Result:")
print(right_join, "\n")