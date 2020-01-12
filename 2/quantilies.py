var = []
import matplotlib.pyplot as plt
file = open('Erl10_1.txt','r')
data = file.read()
data = ''.join(data)
data1 = data.split()
#var.append(sorted(list(map(float,data))))
#print(data, '\n')

file = open('Erl10_2.txt','r')
data = file.read()
data = ''.join(data)
data2 = data.split()
#var.append(sorted(list(map(float,data))))
#print(data, '\n')
file = open('Erl10_3.txt','r')
data = file.read()
data = ''.join(data)
data3 = data.split()
#var.append(sorted(list(map(float,data))))
#print(data, '\n')
file = open('Erl10_4.txt','r')
data = file.read()
data = ''.join(data)
data4 = data.split()
#var.append(sorted(list(map(float,data))))
#print(data, '\n')
file = open('Erl10_5.txt','r')
data = file.read()
data = ''.join(data)
data5 = data.split()
#var.append(sorted(list(map(float,data))))
#print(data, '\n')
#pprint.pprint(var)

"""def quantils(data, f, j, k):
    quant1 = []
    quant2 = []
    quant3 = []
    n1 = int(f * len(data[1]) + 1)
    n2 = int(j * len(data[1]) + 1)
    n3 = int(k * len(data[1]) + 1)
    for i in range(5):
        quant1.append(data[i][n1-1])
    for i in range(5):
        quant2.append(data[i][n2-1])
    for i in range(5):
        quant3.append(data[i][n3-1])
    print('Квантили уровня {} для n = {}'.format(f,len(data[1])), quant1)
    print('Квантили уровня {} для n = {}'.format(j,len(data[1])), quant2)
    print('Квантили уровня {} для n = {}'.format(k,len(data[1])), quant3)

quantils(var, 0.1, 0.5, 0.7)"""

fig = plt.figure()
sb = fig.add_subplot(1, 1, 1)
sb.hist(data1, 100)
sb.hist(data2, 100)
sb.hist(data3, 100)
sb.hist(data4, 100)
sb.hist(data5, 100)

plt.show()