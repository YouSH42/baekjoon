import sys

data = []

n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
for k in range(n):
    total = 0
    for j in data[k]:
        total += j
    total = total - data[k][0]
    averge = total/(len(data[k])-1)
    pass_1 = 0
    for i in range(data[k][0]):
        if data[k][i+1] > averge :
            pass_1 += 1
    percent = pass_1/data[k][0]*100
    print("%0.3f%%" % percent)