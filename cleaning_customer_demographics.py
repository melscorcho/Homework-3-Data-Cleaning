import pandas as pd
import numpy as np

# csv to dataframe
df_demo = pd.read_csv('/workspaces/Homework-3-Data-Cleaning/customer_demographics_contaminated (1).csv')

# print data
print(df_demo.head())
print("\n")

# benchmarking data 
print("Demographics Data Before Cleaning")
initial_demo_rows = len(df_demo)
print("Total rows before cleaning:", initial_demo_rows)
print("How many duplicates are there?", df_demo.duplicated().sum())
print("How many missing values in each column?\n", df_demo.isnull().sum())
print("\n")

# force everything in the Age column to be a number (this changes bad text to NaN)
df_demo['Age'] = pd.to_numeric(df_demo['Age'], errors='coerce')

# anyone older than 120 is a typo replace then with NaN
df_demo.loc[df_demo['Age'] > 120, 'Age'] = np.nan

# fill in missing data with median in oreder not to lose a huge chunk of data
median_age = df_demo['Age'].median()
df_demo['Age'] = df_demo['Age'].fillna(median_age)
print("Filled missing ages with the median:", median_age)

# find the mode and use it for income level nulls
mode_income = df_demo['IncomeLevel'].mode()[0]
df_demo['IncomeLevel'] = df_demo['IncomeLevel'].fillna(mode_income)
print("Filled missing incomes with the mode:", mode_income)


df_demo['SignupDate'] = pd.to_datetime(df_demo['SignupDate'], errors='coerce', format='mixed')

# duplicate rows fix
df_demo = df_demo.drop_duplicates()
print("Dropped the exact duplicates.\n")

# check data after cleaning
print("--- Demographics Data (After) ---")
final_demo_rows = len(df_demo)
print("Total rows left:", final_demo_rows)
print("Rows dropped:", initial_demo_rows - final_demo_rows)
print("Null values left:\n", df_demo.isnull().sum())
print("\n")

# create new file
df_demo.to_csv('/workspaces/Homework-3-Data-Cleaning/customer_demographics_cleaned.csv', index=False)
print("The clean dataset is saved yipeeeee.")