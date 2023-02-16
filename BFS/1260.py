import sys, copy
from collections import deque

def dfs(V, graph, visited):
    visited[V] = True
    print(V, end=" ")
    for i in graph[V]:
        if (visited[i] == False):
            dfs(i, graph, visited)

def bfs(V, graph, visited):
    dq = deque()
    dq.appendleft(V)
    visited[V] = True

    while(dq):
        v = dq.pop()
        print(v, end=" ")
        for i in graph[v]:
            if (visited[i] == False):
                dq.appendleft(i)
                visited[i] = True
    

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
visited[0] = True

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(V, copy.deepcopy(graph), copy.deepcopy(visited))
print()
bfs(V, copy.deepcopy(graph), copy.deepcopy(visited))
