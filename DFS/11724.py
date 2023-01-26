import sys
sys.setrecursionlimit(10**6)

def dfs(i, graph, visited):
    visited[i] = True

    for j in graph[i]:
        if (visited[j] == False):
            dfs(j, graph, visited)
    

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
visited[0] = True
result = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

while (False in visited):
    for i in visited:
        if (i == False):
            result += 1
            dfs(visited.index(i), graph, visited)
print(result)
