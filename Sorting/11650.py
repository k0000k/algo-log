n = int(input())
num = []

for i in range(n):
    temp = list(map(int, input().split()))
    num.append(temp)


num.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print("%d %d"%(num[i][0], num[i][1]))
