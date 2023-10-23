import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import krakenex
import datetime

par='XXBTZEUR'
intervalo=1
###CREAR GRAF CON MATPLOTLIB
def crear_graf(self,df,ind,vol):

    df=df[:45]
    fig, ax =plt.subplots(2,1)
    fig.set_figheight(8)
    fig.set_figwidth(15)
    #define width of candlestick elements
    width = .4
    width2 = .05

    #define up and down prices
    up = df[df.close>df.open]
    eq = df[df.close==df.open]
    down = df[df.close<df.open]

    #define colors to use
    col1 = 'green'
    col2 = 'red'
    # Plotting up prices of the stock 
    ax[0].bar(up.index, up.close-up.open, width, bottom=up.open, color=col1) 
    ax[0].bar(up.index, up.high-up.close, width2, bottom=up.close, color=col1) 
    ax[0].bar(up.index, up.low-up.open, width2, bottom=up.open, color=col1)

    ax[0].bar(eq.index, .5, width, bottom=eq.open, color=col1) 
        
    
    # Plotting down prices of the stock 
    ax[0].bar(down.index, down.close-down.open, width, bottom=down.open, color=col2) 
    ax[0].bar(down.index, down.high-down.open, width2, bottom=down.open, color=col2) 
    ax[0].bar(down.index, down.low-down.close, width2, bottom=down.close, color=col2)
    plt.xticks([])

    if vol:
        ax[1].bar(up.index,up.volume,width,bottom=0,color=col1)
        ax[1].bar(down.index,down.volume,width,bottom=0,color=col2)

    return fig