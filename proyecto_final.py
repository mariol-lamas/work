import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import krakenex
import datetime
from bokeh.plotting import figure, column
from bokeh.models import NumeralTickFormatter
class App():
    
    def __init__(self) -> None:
        self.kraken=krakenex.API()
        self.par_wsname=self.obtener_pares()
        self.names=self.par_wsname.keys()
        self.intervalos={'1m':1,'15m':15,'30m':30,'1h':60,'24h':60*24}
               

    def obtener_pares(self):
        '''
        Función encargada de la obtención de los pares de divisas disponibles
        en la API de Kraken.

        Devuelve el nombre del par en 2 formatos:
        Wsname --> BTC / EUR
        Nombre_técnico --> 
        '''
        result=self.kraken.query_public('AssetPairs')['result']
        valores = result.keys()

        dic={}
        for elem in valores:
            dic[result[elem]['wsname']]=elem
        return dic
    
    def barra_lat(self):
        '''
        Funcion encargada de la definición de los elementos de 
        la barra lateral.

        Devuelve:
        Divisa --> Se corresponde con el nombre del par divisa en formato wsname
        Intervalo --> 
        Indicadores --> Devuelve los indicadores a mostrar en el gráfico
        '''
        with st.sidebar:
            st.write('Opciones del gráfico')
            divisa=st.selectbox(
                'Par de divisas',
                ('BTC/EUR','BTC/USD','ETH/EUR','ETH/USD','ETH/BTC')
            )
            intervalo = st.selectbox(
                    'Intervalo',
                    ('1m', '15m', '30m','1h','24h'),
                    index=0)
            indicadores = st.multiselect(
                    'Indicadores',
                    ['VWAP', 'STOCH', 'BANDS', 'IND-D'],
                    [],)
            
            vol=st.checkbox('Mostrar volumen')
        return divisa,intervalo,indicadores, vol
    
    def obt_datos(self,par,intervalo):
        '''
        Se encarga de realizar la query a la API de kraken para obtener los datos a partir del par de divisas
        y del intervalo de datos ya que estas queries devuelven un máximo de 720 valores.
        Devuelve -> Dataframe con columnas ['timestamp','open','high','low','close','volume','conteo']
        '''
        ohlc_data = self.kraken.query_public('OHLC', {'pair': par,'interval':intervalo})
        try:
            ohlc_list = ohlc_data['result']
            df=pd.DataFrame(ohlc_list[par],columns=['timestamp', 'open', 'high','low','close','_','volume','conteo'])
            df['Date']=df['timestamp'].map(lambda x: datetime.datetime.fromtimestamp(x))
            df['Date_str']=df['Date'].astype(str)
            df['color']=df[['close','open']].apply(lambda x: 'red' if x.open>x.close else 'green',axis=1 )
            df['open']=df['open'].astype(float)
            df['close']=df['close'].astype(float)
            df['high']=df['high'].astype(float)
            df['low']=df['low'].astype(float)
            df['volume']=df['volume'].astype(float)
            df['Cum_Vol'] = df.iloc[::-1]['volume'].cumsum()
            df['m']=(df['close'])*df['volume']
            df['m_cum']=df.iloc[::-1]['m'].cumsum()
            #df['Cum_Vol_Price'] = (df['volume'] * (df['high'] + df['low'] + df['close'] ) /3).cumsum()
            df['VWAP'] = df['m_cum'] / df['Cum_Vol']
            '''
            df['slowk'],df['slowd']=ta.STOCH(df['high'],df['low'],df['close'],
                                             slowk_period=3,slowk_matype=0,
                                             slowd_period=3,slowd_matype=0)
            df['upper_band'],_,df['lower_band']=ta.BBANDS(df['close'],timeperiod=20)
            '''            
            return df
        
        except KeyError:
            st.write('No se dispone de información del par de divisas escogido')
            return pd.DataFrame([])

    def crear_graf(self,df,ind,vol,div):
        df=df[::-1]
        df_reduce=df[:46].copy()
        start=df_reduce['Date'].values.min()
        end=df_reduce['Date'].values.max()
        
        candle=figure(x_axis_type='datetime',height=300,x_range=(df['Date'].values[-1],df['Date'].values[0]),
                      tooltips=[('Date','@Date_str'),('open','@open'),('close','@close'),('high','@high'),('low','@low'),
                                ('color','@color')],y_axis_label='Precio',toolbar_location=None,
                                title=f'{div}')
    
        candle.segment('Date','low','Date','high',color='black',line_width=.5,source=df)
        candle.segment('Date','open','Date','close',color='color',line_width=6,source=df)
        candle.title.align='center'
        candle.title.text_font_size='16pt'

        if 'VWAP' in ind:
            candle.line('Date', 'VWAP', line_color="blue", line_width=.5, legend_label="VWAP-",source=df)
        candle.x_range.start= start
        candle.x_range.end= end
        children=[candle]
        volumen=None
        if vol:
            volumen=figure(x_axis_type='datetime',height=120,x_range=(df['Date'].values[-1],df['Date'].values[0]),y_axis_label='Volumen',
                           toolbar_location=None)
            volumen.segment('Date',0,'Date','volume',color='color',line_width=6,source=df)
            volumen.yaxis.formatter = NumeralTickFormatter(format="0")
            volumen.x_range=candle.x_range
            children.append(volumen)
        '''
        if 'STOCH' in ind:
            estocast=figure(x_axis_type='datetime',height=100,x_range=(df['Date'].values[-1],df['Date'].values[0]),y_axis_label='STOCH',
                            toolbar_location=None)
            estocast.line('Date','slowk',line_color='blue',line_width=.5,legend_label='slowk',source=df)
            estocast.line('Date','slowd',line_color='orange',line_width=.5,legend_label='slowd',source=df)
            estocast.x_range=candle.x_range
            children.append(estocast)
        
        if 'BANDS' in ind:
            candle.line('Date','upper_band',line_color='green',line_width=.5,source=df)
            candle.line('Date','lower_band',line_color='red',line_width=.5,source=df)
            candle.varea('Date', 'upper_band', 'lower_band', fill_color="gray", alpha=0.5,source=df)
        '''
            


        return column(children=children,sizing_mode='scale_width')

    def centro(self,fig):
        st.header("INTERACTIVE TRADING VIEW     BTC & ETH", divider='rainbow')
        st.bokeh_chart(fig,use_container_width=True)
    
    def run(self):
        st.set_page_config(page_title='INTERACTIVE TRADING VIEW') 
        divisa, intervalo, indicadores, vol=self.barra_lat()
        dataframe=self.obt_datos(divisa,self.intervalos[intervalo])   #'XXBTZEUR'
        if not dataframe.empty:
            fig=self.crear_graf(dataframe,indicadores,vol,divisa)
            self.centro(fig)



if __name__=='__main__':
    app=App()
    app.run()

