

def mostr(funcion):
    def mostr_dec(a,b):

        print('Mostradndo las infoeslkad')
        funcion(a,b)
        print('Funcion ha sido ejecutada')
    
    return mostr_dec
@mostr
def sum(a,b):
    print('Esto es una suma')
    print(a+b)
import math
class Primes():
    @staticmethod
    def stream():
        def es_primo(n):
            return not any(n % i == 0 for i in range(3, int(n**0.5) + 1, 2))
        num=2
        yield num
        num=3
        while True:
            if es_primo(num):
                yield num
            num+=2



class Primes():
    @staticmethod
    def stream():
        yield 2  # El primer número primo es 2
        yield 3  # El segundo número primo es 3
        primes = [2, 3]
        num = 5
        while True:
            is_prime = True
            sqrt=int(num ** 0.5)
            for prime in primes:
                if prime > sqrt:
                    break
                if (num % prime == 0):
                    is_prime=False
                    break
            if is_prime:
                primes.append(num)
                yield num
            num += 2
def generate_primes(n):
        # Sieve of Eratosthenes algorithm
        is_prime = [False, False] + [True for x in range(2, n + 1)] 
        i = 2
        while i * i <= n:

            if is_prime[i]:
                for j in range(i*2, n+1, i):
                    is_prime[j] = False
            i += 1

        primes = [x for x in range(n+1) if is_prime[x]]

        return primes
class Primes:
    
    primos=generate_primes(16000000)
    
    @staticmethod
    def stream():
        yield from Primes.primos


def smaller(arr):
    res=[]
    val=len(arr)
    for id,elem in enumerate(arr):
        if id!=val-1:
            valor=list(map(lambda x: 1 if x<elem else 0,arr[id+1:])).count(1)
            res.append(valor)
        else:
            res.append(0)
    
    return res
import re
class Inspector:
    def __init__(self) -> None:
        self.per=[]
        self.den=[]
    def receiveBulletin(self,string):
        for line in string.split('\n'):
            prim_pal=line.split(' ')[0]
            if prim_pal=='Allow' or prim_pal=='Deny':
                res=re.findall(r'[o]+[f]+\s.*',string)[0].replace(' ','')[2:].split(',')
                if prim_pal=='Allow':
                    self.per.extend(res)
                else:
                    self.den.extend(res)
        print('Permitidos: ', self.per,
              '\nDenegados: ',self.den)
        
    def inspect():
        ... 

from functools import reduce
from math import pow

def closest_pair(points):
    minimo=((points[0][0]-points[1][0])**2+(points[0][1]-points[1][1])**2)
    valores=(points[0],points[1])
    for id1,res1 in enumerate(points):
        for id2,res2 in enumerate(points):
            val=((res1[0]-res2[0])**2 + (res1[1]-res2[1])**2)
            if minimo>val and (id1!=id2):
                minimo=val
                valores=(res1,res2)
    return valores
            

points = (
            (2, 2), # A
            (2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  # G
        )

import time
inicio=time.time()
print(closest_pair(points))
fin=time.time()
print('Tiempo: ',fin-inicio)



