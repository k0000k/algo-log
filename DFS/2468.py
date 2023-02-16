import sys
import copy

sys.setrecursionlimit(10**6)

def dfs(a, b, copy_ground, rain):
    copy_ground[a][b] = False

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        if (0 <= a + dx[i] <= len(copy_ground) - 1 and 0 <= b + dy[i] <= len(copy_ground) - 1 ):
            if (copy_ground[a + dx[i]][b + dy[i]] > rain):
                dfs(a + dx[i], b + dy[i], copy_ground, rain)

cnt = int(sys.stdin.readline())
ground = []
min_val = 100
max_val = 1
results = []

for i in range(cnt):
    temp = list(map(int, sys.stdin.readline().split()))
    temp_min = min(temp)
    temp_max = max(temp)
    ground.append(temp)

    if (temp_min < min_val):
        min_val = temp_min
    if (temp_max > max_val):
        max_val = temp_max
    
for i in range(min_val - 1, max_val + 1):
    result = 0
    copy_ground = copy.deepcopy(ground)

    for a in range(cnt):
        for b in range(cnt):
            if (copy_ground[a][b] != False):
                if (copy_ground[a][b] <= i):
                    copy_ground[a][b] = False
                else:
                    dfs(a, b, copy_ground, i)
                    result += 1
    results.append(result)

print(max(results))


