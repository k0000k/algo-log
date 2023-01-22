import sys
import heapq

h = []
cnt = int(input())

for i in range(cnt):
    num = int(sys.stdin.readline().rstrip())

    if (num == 0):
        if (len(h) == 0):
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, num)
