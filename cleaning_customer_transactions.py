import pandas as pd
import numpy as np

df_trans = pd.read_csv('/workspaces/Homework-3-Data-Cleaning/customer_transactions_contaminated (1).csv')

# benchmark
print("Transactions Data Before Cleaning")
initial_trans_rows = len(df_trans)
print("Total rows before cleaning:", initial_trans_rows)
print("How many duplicates are there?", df_trans.duplicated().sum())
print("How many missing values in each column?\n", df_trans.isnull().sum())
print("\n")

# cleaning, drop duplicates, fill missing values, standardized format 
df_trans = df_trans.drop_duplicates()
print("Dropped exact duplicates.\n")

df_trans['Amount'] = pd.to_numeric(df_trans['Amount'], errors='coerce')
median_amount = df_trans['Amount'].median()
df_trans['Amount'] = df_trans['Amount'].fillna(median_amount)
print("Filled missing amounts with median to keep structural integrity")
print("amount filled in:", median_amount)

df_trans['ProductCategory'] = df_trans['ProductCategory'].fillna('Other')
print("Missing product categories replaced with Other to keep rows.")

df_trans['TransactionDate'] = pd.to_datetime(df_trans['TransactionDate'], errors='coerce', format='mixed')
df_trans['ProductCategory'] = df_trans['ProductCategory'].str.strip().str.title()
df_trans['PaymentMethod'] = df_trans['PaymentMethod'].str.strip().str.title()
print("Fixed the text columns.")

# checking the data after cleaning
print("\n--- Transactions Data (After) ---")
final_trans_rows = len(df_trans)
print("Total rows left:", final_trans_rows)
print("Rows dropped:", initial_trans_rows - final_trans_rows)
print("Null values left:\n", df_trans.isnull().sum())
print("\n")

# saving to new file
df_trans.to_csv('/workspaces/Homework-3-Data-Cleaning/customer_transactions_cleaned.csv', index=False)
print("The clean transactions dataset is saved yipeeeee.")