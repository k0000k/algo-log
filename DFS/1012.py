import sys

sys.setrecursionlimit(10**6)

def dfs(y, x, land):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    land[y][x] = 0

    for i in range(4):
        if (0 <= y + dy[i] <= len(land) - 1 and 0 <= x + dx[i] <= len(land[y]) - 1):
            if (land[y + dy[i]][x + dx[i]] == 1):
                land[y + dy[i]][x + dx[i]] = 0
                dfs(y + dy[i], x + dx[i], land)


testcases = int(sys.stdin.readline())

for i in range(testcases):
    M, N, cnt = map(int, sys.stdin.readline().split())
    land = [[0 for a in range(M)] for b in range(N)]

    for j in range(cnt):
        x, y = map(int, sys.stdin.readline().split())
        land[y][x] = 1
    
    result = 0
    for y in range(N):
        for x in range(M):
            if (land[y][x] == 1):
                dfs(y, x, land)
                result += 1
    
    print(result)
