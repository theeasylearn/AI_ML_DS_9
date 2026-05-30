import mplfinance as mpf 
import pandas as pd 
import datetime as dt 
df = pd.read_csv('nifty50.csv').squeeze()
stock = pd.DataFrame({
    'Date': df['Date'],
    'Open': df['Open'],
    'High': df['High'],
    'Low': df['Low'],
    'Close': df['Close']
})
stock['Date'] = pd.to_datetime(stock['Date'], dayfirst=True)
# 2. Set the 'Date' column as the index to create a DatetimeIndex
stock.set_index('Date', inplace=True)
mpf.plot(stock,type='candle',style='yahoo')

