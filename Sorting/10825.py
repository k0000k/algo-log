import sys

cnt = int(sys.stdin.readline())
persons = []

for i in range(cnt):
    temp = list(sys.stdin.readline().rstrip().split())
    persons.append(temp)

persons.sort(key= lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in persons:
    print(i[0])
