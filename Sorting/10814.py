import sys

cnt = int(sys.stdin.readline())
persons = []

for i in range(cnt):
    temp = list(sys.stdin.readline().rstrip().split())
    temp.append(i)
    persons.append(temp)

persons.sort(key= lambda x: (int(x[0]), x[2]))

for i in persons:
    print(i[0], i[1])
