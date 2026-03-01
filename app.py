import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("Preprocessing3.csv")
print(df.head())
print(df.shape)

#print(df.info())

#print(df.describe())

#print(df.isna().sum())
df['Date']=pd.to_datetime(df["Date"])
print(df['Date'].max())
print(df['Date'].min())
#print(df['Date'].dt.day)
#df.info()


# --- Date feature extract day,month, year from that -----
new_df=pd.DataFrame(df['Date'])
print(new_df.head())
new_df['Month']=df['Date'].dt.month
new_df['Year']=df['Date'].dt.year
new_df['Day']=df['Date'].dt.day
print(new_df.head())
print(new_df.tail())



#--- extract stock data------

import yfinance as yf
ticker_symbol='RELIANCE.NS'
stock_data=yf.download(ticker_symbol,start='2024-01-01',end='2025-08-01',interval='1d')
print(stock_data)

stock_data["Close"].plot()
print(plt.show())