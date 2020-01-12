# -*- coding: utf-8 -*-


from numpy import random as npr


def Erl(k):
    x = 0;
    for i in range(k):
        x += npr.exponential(1)
    return x

"""n = 1000    
file = open('ErlDistr.txt','w')  #Код для 1 дз
for i in range(n):
    file.write(str(Erl(30))+' ')
    
    """
smp = [5,10,100,1000,100000]   #Код для 2 дз
for i in range(len(smp)):
    for j in range(1,6):
        file = open('Erl{}.txt'.format('{}_{}'.format(smp[i], j)), 'w')
        for k in range(smp[i]):
             file.write(str(Erl(30))+' ')   
