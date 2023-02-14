import sys

sys.setrecursionlimit(10**6)

def dfs(i, j, rect, result):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    rect[i][j] = 1
    result += 1

    for a in range(4):
        if (0 <= i + dx[a] <= len(rect) - 1 and 0 <= j + dy[a] <= len(rect[i]) - 1):
            if (rect[i + dx[a]][j + dy[a]] == 0):
                rect[i + dx[a]][j + dy[a]] = 1
                result = dfs(i + dx[a], j + dy[a], rect, result)
    return result

M, N, K = map(int, sys.stdin.readline().split())
rect = [[0 for i in range(N)] for j in range(M)]

for i in range(K):
    left_x, left_y, right_x, right_y = map(int, sys.stdin.readline().split())

    for a in range(left_y, right_y):
        for b in range(left_x, right_x):
            rect[a][b] = 1

results = []
for i in range(M):
    for j in range(N):
        if (rect[i][j] == 0):
            result = 0
            result = dfs(i, j, rect, result)
            results.append(result)

print(len(results))
results.sort()

for i in results:
    print(i, end=" ")

