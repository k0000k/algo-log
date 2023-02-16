import sys
from collections import deque

def bfs(a, b, families, visited):
    result = 0
    visited[a] = True
    dq = deque()
    dq.appendleft((a, 0))

    while (dq):
        v = dq.pop()
        if (v[0] == b):
            return v[1]
        for i in families[v[0]]:
            if (visited[i] == False):
                visited[i] = True
                dq.appendleft((i, v[1] + 1))
    return -1

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
families = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
visited[0] = True

for i in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    families[parent].append(child)
    families[child].append(parent)

result = bfs(a, b, families, visited)
print(result)
