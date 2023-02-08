import heapq, sys

hq = []
result = 0

cnt = int(sys.stdin.readline())

for i in range(cnt):
    heapq.heappush(hq, int(sys.stdin.readline()))

while (len(hq) != 1):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    result += (a + b)
    heapq.heappush(hq, a + b)

print(result)
