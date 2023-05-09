import sys, math

N = int(sys.stdin.readline())

fact = 1
cnt_5 = 0
for i in range(1, N + 1):
    fact *= i

    while (i % 5 == 0):
        i = i // 5
        cnt_5 += 1

print(str(fact)[-cnt_5 - 1])

