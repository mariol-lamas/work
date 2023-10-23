import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import krakenex
import datetime

par='XXBTZEUR'
intervalo=1

kraken=krakenex.API()
ohlc_data = kraken.query_public('OHLC', {'pair': par,'interval':intervalo})
ohlc_list = ohlc_data['result']
df=pd.DataFrame(ohlc_list[par],columns=['timestamp', 'open', 'high','low','close','_','volume','conteo'])
#df=pd.read_csv('/Users/malamas/Desktop/Proyecto_py_krakenAPI/BTC_cot.csv',sep=';')

df['open']=df['open'].apply(lambda x: float(x))
df['close']=df['close'].apply(lambda x: float(x))
df['high']=df['high'].apply(lambda x: float(x))
df['low']=df['low'].apply(lambda x: float(x))

df['timestamp']=df['timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(x))
df['Bar color']=df[['open','close']].apply(lambda x: 'red' if x.open > x.close else 'green',axis=1)

df=df[:3]
print(df)
fig, ax =plt.subplots()
col1='red'
col2='green'

up=df[df.open>=df.close]
down=df[df.open<df.close]
width = .3
width2 = .03

  
# Plotting up prices of the stock 
print(up.open-up.close)
ax.bar(up.timestamp, up.open - up.close, width, bottom=up.open, color=col1) 
ax.bar(up.timestamp, up.high-up.close, width2, bottom=up.close, color=col1) 
ax.bar(up.timestamp, up.low-up.open, width2, bottom=up.open, color=col1) 
  
# Plotting down prices of the stock 
'''
ax.bar(down.timestamp, down.close-down.open, width, bottom=down.open, color=col2) 
ax.bar(down.timestamp, down.high-down.open, width2, bottom=down.open, color=col2) 
ax.bar(down.timestamp, down.low-down.close, width2, bottom=down.close, color=col2) 
'''
  
# displaying candlestick chart of stock data  
# of a week 
plt.yscale('linear')
plt.xticks(rotation=30,ha='right')
plt.show()
#st.pyplot(fig=fig)