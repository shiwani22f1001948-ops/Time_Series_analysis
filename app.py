import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("Preprocessing3.csv")
print(df.head())
print(df.shape())

print(df.info())

print(df.describe())

print(df.isna().sum())