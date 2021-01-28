import numpy as np
import time

def Geom(p):  #Функция генерации псевдосл. величины
    a, b, c = 0, 0, 0
    while a == 0:
        c = np.random.rand()
        if c < p:
            a = 1
        else:
            b = b + 1
    return b  


"""file = open("GeomDistr.txt", "w")
for i in range(1000000):
    file.write(str(Geom(0.2)) + " ")
file.close()"""
file = open("GeomDistr.txt", "r")
file = list(map(int, file.split()))
mean = 0
for i in file:
    mean += i
mean = mean/len(file)
print("Var Mean : ", mean)











"""smp = [5,10,100,1000,1000000]   #Код для 2 дз
for i in range(len(smp)):
    current_time = time.time()
    for j in range(1,6):
        file = open('Geom{}.txt'.format('{}_{}'.format(smp[i], j)), 'w')
        for k in range(smp[i]):
             file.write(str(Geom(0.2))+' ')
    print(time.time() - current_time)   """