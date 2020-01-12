from random import random, randint
from math import e, log
import matplotlib.pyplot as plt

def U(a, b):
    return a + random() * (b-a)

__x1 = 7.69711747013104972
__A = 3.9496598225815571993e-3
__sW = list(None for i in range(257))
__sH = list(None for i in range(256))

def setupExpTables():
    """coordinates of the implicit rectangle in base layer"""
    __sH[0] = e**(-__x1)
    __sW[0] = __A / __sH[0]
    """implicit value for the top layer"""
    __sW[256] = 0
    for i in range(1, 256):
        """such x_i that f(x_i) = y_{i-1}"""
        __sW[i] = -log(__sH[i - 1])
        __sH[i] = __sH[i - 1] + (__A / __sW[i])

def ExpZiggurat():
    itr = 0
    while itr <= 10^10:
        __sId = randint(0, 255)
        __x = U(0, __sW[__sId])
        if (__x < __sW[__sId + 1]):
            return __x
        if __sId == 0:
            return __x1 + ExpZiggurat()
        if U(__sH[__sId - 1], __sH[__sId]) < e**(-__x):
            return __x
    else:
        return None


def Exponential(rate):
    return ExpZiggurat() / rate

setupExpTables()

def Erlang(k, T):
    x = 0
    for i in range(k):
        x += Exponential(T)
    return x

for j in range(100):
    plt.scatter(0, Erlang(4, 4))

plt.show()