import numpy as np
import math
smp = [5,10,100,1000,10000]
data = []
def same(k):
    mas = []
    for i in k:
        if i not in mas:
            mas.append(i)
    return(mas)        
def f(a,b):
    s = 0
    for i in range(len(a)):
        if a[i] < b:
            s += 1
        else:
            break
    return(s / len(a))
for k1 in range(len(smp)):
    var = []
    maxs = []
    for i in range(len(smp)):
        file = open('Erl{}_{}.txt'.format(smp[k1], i+1),'r')
        data = file.read()
        data = ''.join(data)
        data = data.split()
        var.append(sorted(list(map(float,data))))
    for i in range(4):
        for j in range(i+1, 5):
            max = -100000    
            mas = sorted(np.concatenate([var[i], var[j]]))
            for k in range(len(mas)):
                if math.fabs(f(var[i], mas[k]) - f(var[j], mas[k])) > max:
                   max = math.fabs(f(var[i], mas[k]) - f(var[j], mas[k]))
            maxs.append(max)
    print("n = {}".format(smp[k1]), maxs, '\n')