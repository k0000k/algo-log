N = int(input())
times = list(map(int, input().split()))
times.sort()

current_max = 0
sum = 0

for i in range(N):
    current_max += times[i]
    sum += current_max

print(sum)
