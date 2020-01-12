from random import random, randint
from math import exp, log
import matplotlib.pyplot as plt

def Unif(a, b):
    return a + random() * (b-a)


def Log(p):
    V = Unif(0,1)
    if V >= p:
        return(1.0)
    U = Unif(0,1)
    y = 1.0 - exp(U / (1.0 / log(1.0 - p)))
    if V > y:
        return(1.0)
    if V <= y * y:
        return round(1.0 + log(V) / log(y))
    return(2.0)
 
n = 10000    
file = open('Distr.txt','w')  #Код для 1 дз
for i in range(n):
    file.write(str(Log(0.8))+' ')
plt.show()