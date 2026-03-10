# make repository
# make folder in Document Folder
# open that folder on Git Bash
# write on git bash "git clone reporsitory-Http-url"
# write "code ." to open  that file on vs-code 
# ls;  after cloning your repository name visible on your bash when you write ls on vs terminal
# cd repository-name
# now make file and run the code python file.py


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
print(type(stock_data))
print(stock_data.columns)

#stock_data["Close"].plot()
#stock_data["Open"].plot()
#plt.show()


#------ Time Resampling --------
# resample() command used to change the time frequency of time-series data.It mainly used when dataset has a date/time index.
import pandas as pd
print(pd.date_range(start="07-1-2025",end="7-30-2025",freq='W'))   # W=Weekly frequency ( all other information given in python document)
df1=pd.read_csv("Nifty 50 Historical Data.csv")
print(df1.info())
print(df1.head())
df2=pd.read_csv("Nifty 50 Historical Data.csv",parse_dates=["Date"],index_col="Date")# parse_dates convert "Date feature into datetime format" # index_col set "Date" feature as index
print(df2.info())
print(df2.head())
df2=df2.rename(columns={"Price":"Close"})
print(df2.head())
print(df2.iloc[0])  # give index 0( row) data
print(df2.sort_index())# sort index to confirm date are in increasing order

# resample() groups time data into different time intervals(day,week,month,etc) and thenn applies a function like sum, mean, max etc.
df2["Close"]=df2["Close"].str.replace(",","").astype(float)
print(df2.info())
#df2["Close"].resample(rule="M").mean()  # it represent "M" monthwise avg of Close value
df2["Close"].resample(rule="ME").mean().plot(kind="bar")
df2["Close"].resample(rule="YE").mean().plot(kind="bar",figsize=(12,5))
plt.show()

