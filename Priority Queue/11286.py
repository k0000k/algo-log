import sys
import heapq

h = []
absolute_h = []

cnt = int(sys.stdin.readline().rstrip())

for i in range(cnt):
    num = int(sys.stdin.readline().rstrip())

    if (num == 0):
        if (len(h) == 0):
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(num), num))
