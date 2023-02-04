import heapq
import sys

cnt = int(sys.stdin.readline())
hq = []

for i in range(cnt):
    idx, h = map(int, sys.stdin.readline().split())
    heapq.heappush(hq, (-h, idx))

right = left = heapq.heappop(hq)
sum = -right[0]

while (len(hq) != 0):
    temp = heapq.heappop(hq)

    if (temp[1] > right[1]):
        sum = sum + (temp[1] - right[1]) * (-temp[0])
        right = temp
    elif (temp[1] < left[1]):
        sum = sum + (left[1] - temp[1]) * (-temp[0])
        left = temp
print(sum)
