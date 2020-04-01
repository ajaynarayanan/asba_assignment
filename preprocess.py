import pandas as pd
import numpy as np

df = pd.read_csv("plants.csv",)
print("Number of records in df = ", len(df), end ="\n\n")
print("====================== Sample records ====================== ")
print(df.head(), end ="\n\n")
print("====================== Statistics of data ====================== ")
print(df.describe())

print("====================== Total number of NAN values per column ====================== ")
print(df.isnull().sum(axis = 0))
print("====================== Replacing nan with mode  ====================== ")
# Mode computation ignores NAN 
for column in df:
    df[column] = df[column].fillna(df[column].mode()[0])

print("====================== Statistics of data ====================== ")
print(df.describe())

print("====================== Total number of NAN values per column ====================== ")
print(df.isnull().sum(axis = 0))

df.to_csv("plant.csv", encoding='utf-8', index=False)
