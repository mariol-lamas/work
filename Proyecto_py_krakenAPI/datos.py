import krakenex
import datetime
import pandas as pd
#import streamlit as st
import matplotlib.pyplot as plt
import talib as ta
# Crear una instancia del cliente Kraken
#st.set_page_config(page_title='Cryptochange',layout='wide')

def capturar_datos(par,intervalo):
    kraken = krakenex.API()
    ohlc_data = kraken.query_public('OHLC', {'pair': par,'interval':intervalo})
    ohlc_list = ohlc_data['result']
    df=pd.DataFrame(ohlc_list[par],columns=['timestamp', 'open', 'high','low','close','_','volume','conteo'])
    df['timestamp']=df['timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    df['Bar color']=df[['open','close']].apply(lambda x: 'red' if x.open > x.close else 'green',axis=1)


    return df

def crear_graf(df,mostrar_vol=False, indicadores=[]):
    ...





# Definir el par de criptomonedas y el intervalo de tiempo
pair = 'XXBTZEUR'  # Por ejemplo, Bitcoin (BTC) frente al dólar estadounidense (USD)
interval = 1    # Intervalo de tiempo (1d para datos diarios)

df=pd.read_csv('/Users/mariolamas/Desktop/work-1/Proyecto_py_krakenAPI/BTC_cot.csv',sep=';')
print(df.keys())

#print(ta.SMA(df['close'].values,8))
df['RSI']=ta.MA(df['close'].values,10)
print('\n',df.tail())

print(capturar_datos(pair,interval))

