import numpy
import math

n = 1000000
def Log(p):
    rate = math.log1p(p)
    n = numpy.random.logseries(rate)
    return n



file = open("LogDist.txt", "w")
for i in range(n):
    file.write(str(Log(0.7)) + " ")

sample =[5, 10, 100, 1000, 10000]
for i in range(len(sample)):
    for j in range(1, 6):
        file = open("Log{}.txt".format("{}_{}".format(sample[i], j)), 'w')
        for k in range(sample[i]):
            file.write(str(Log(0.7)) + " ")