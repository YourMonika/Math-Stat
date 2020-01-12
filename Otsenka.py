num = [5, 10, 100, 1000, 10000]
for i in range(5):
    disp = []
    mean = []
    data = []
    for j in range(len(num)):
        with open("Erl{}.txt".format("{}_{}".format(num[i], j+1))) as f:
            for line in f:
                data.append(list([float(x) for x in line.split()]))
    for k in range(len(data)):
        #mean = sum(data[k])/len(data[k])
        mean.append(sum(data[k]) / len(data[k]))
        #print("Выборочное среднее при n = {}:".format(len(data[k])), mean)
    for m in range(5):
        summ = 0
        for n in range(len(data[m])):
            summ += (data[m][n] - mean[m])**2
        disp.append(summ/len(data[m]))
    for o in range(len(disp)):
        print("Дисперсия при n = {}".format(len(data[1])), disp[o])