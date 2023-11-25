m = int(input())
n = int(input())
list1 = []

num = 1
while(num * num <= n):
    if (m <= num * num <= n):
        list1.append(num * num)
    num += 1

if (not list1):
    print(-1)
else:
    print(sum(list1))
    print(list1[0])

