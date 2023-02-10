impost sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n + 1):
    while (i % 5 == 0):
        i /= 5
        cnt += 1
print(cnt)
