import sys

n = int(input())
num = []

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    num.append(temp)


num.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print("%d %d"%(num[i][0], num[i][1]))
