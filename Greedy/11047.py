import sys

N, K = map(int, input().split())
values = []
min_value = 0

for i in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if (temp > K):
        continue
    else:
        values.append(temp)
    

for i in range(len(values) - 1, -1, -1):
    min_value = min_value + (K // values[i])
    K = K % values[i]
print(min_value)
