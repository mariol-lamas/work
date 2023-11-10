song = '''
Just a small town girl living in a lonely world
She took the midnight train going anywhere
Just a city boy born and raised in South Detroit
He took the midnight train going anywhere

A singer in a smoky room
A smell of wine and cheap perfume
For a smile they can share the night
It goes on and on and on and on

Strangers waiting up and down the boulevard
Their shadows searching in the night
Streetlights, people, living just to find emotion
Hiding somewhere in the night

Working hard to get my fill
Everybody wants a thrill
Payin' anything to roll the dice
Just one more time
Some will win, some will lose
Some were born to sing the blues
Oh, the movie never ends
It goes on and on and on and on

Strangers waiting up and down the boulevard
Their shadows searching in the night
Streetlights, people, living just to find emotion
Hiding somewhere in the night

Don't stop believing
Hold on to that feeling
Streetlights, people
Don't stop believing
Hold on
Streetlights, people
Don't stop believing
Hold on to that feeling
Streetlights, people
'''
from collections import Counter
import pandas as pd

def est(song):

    lineas=song.split('\n')
    df2=pd.DataFrame(list(set(lineas)),columns=['linea'])
    df2['repeticiones']=df2['linea'].apply(lambda x: lineas.count(x))
    df2['posicion']=df2['linea'].apply(lambda x: lineas.index(x))
    df2=df2[df2['repeticiones']>=2]
    df2=df2.sort_values(by='posicion')

    return df2


print(est(song))