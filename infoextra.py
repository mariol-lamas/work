'''
# check if the library folder already exists, to avoid building everytime you load the pahe
if not os.path.isdir("/tmp/ta-lib"):

    # Download ta-lib to disk
    with open("/tmp/ta-lib-0.4.0-src.tar.gz", "wb") as file:
        response = requests.get(
            "http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz"
        )
        file.write(response.content)
    # get our current dir, to configure it back again. Just house keeping
    default_cwd = os.getcwd()
    os.chdir("/tmp")
    # untar
    os.system("tar -zxvf ta-lib-0.4.0-src.tar.gz")
    os.chdir("/tmp/ta-lib")
    # build
    os.system("./configure --prefix=/home/appuser")
    os.system("make")
    # install
    os.system("make install")
    # install python package
    os.system(
        'pip3 install --global-option=build_ext --global-option="-L/home/appuser/lib/" --global-option="-I/home/appuser/include/" ta-lib'
    )
    # back to the cwd
    os.chdir(default_cwd)
    print(os.getcwd())
    sys.stdout.flush()

# add the library to our current environment
from ctypes import *

lib = CDLL("/home/appuser/lib/libta_lib.so.0")
import talib as ta
'''

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


'''
            df['slowk'],df['slowd']=ta.STOCH(df['high'],df['low'],df['close'],
                                             slowk_period=3,slowk_matype=0,
                                             slowd_period=3,slowd_matype=0)
            df['upper_band'],_,df['lower_band']=ta.BBANDS(df['close'],timeperiod=20)
            '''   

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