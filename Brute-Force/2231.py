num = int(input())

for i in range(1, num+1):
    sum = i
    i = str(i)
    for j in i:
        j = int(j)
        sum += j
    if (sum == num):
        print(i)
        break
else:
    print(0)
