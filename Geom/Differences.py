num = [5, 10, 100, 1000, 10000]
for i in range(5):
    disp = []
    data = []
    for j in range(len(num)):
        with open("{}_{}.txt".format(num[i], j+1)) as f:
            for line in f:
                data.append(list([float(x) for x in line.split()]))
    for k in range(len(data)):
        mean = sum(data[k]) / len(data[k])
        print("Разница при n = {}:".format(len(data[k])), abs(0.2 - 1/(1+mean)))