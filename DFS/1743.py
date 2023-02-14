import sys

sys.setrecursionlimit(10**6)

def dfs(i, j, road, result):
    road[i][j] = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    result += 1
    for k in range(4):
        if (0 <= i + dx[k] <= len(road) - 1 and 0 <= j + dy[k] <= len(road[i]) - 1):
            if (road[i + dx[k]][j + dy[k]] == 1):
                result = dfs(i + dx[k], j + dy[k], road, result)
    return result


N, M, cnt = map(int, sys.stdin.readline().split())
road = [[0 for i in range(M)] for j in range(N)]
results = []

for i in range(cnt):
    x, y = map(int, sys.stdin.readline().split())
    road[x - 1][y - 1] = 1

for i in range(N):
    for j in range(M):
        if (road[i][j] == 1):
            result = 0
            result = dfs(i, j, road, result)
            results.append(result)

print(max(results))

