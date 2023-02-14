import sys

sys.setrecursionlimit(10**6)

def dfs(i, j, picture):
    val = picture[i][j]
    picture[i][j] = False

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for a in range(4):
        if (0 <= i + dx[a] <= len(picture) - 1 and 0 <= j + dy[a] <= len(picture) - 1):
            if (picture[i + dx[a]][j + dy[a]] == val):
                dfs(i + dx[a], j + dy[a], picture)

cnt = int(sys.stdin.readline())

color3 = []
color2 = []


for i in range(cnt):
    temp = sys.stdin.readline().rstrip()
    temp3 = []
    temp2 = []

    for j in temp:
        temp3.append(j)

        if (j == "B"):
            temp2.append(2)
        else:
            temp2.append(1)

    color2.append(temp2)
    color3.append(temp3)

result2 = 0
for i in range(cnt):
    for j in range(cnt):
        if (color2[i][j] != False):
            dfs(i, j, color2)
            result2 += 1

result3 = 0
for i in range(cnt):
    for j in range(cnt):
        if (color3[i][j] != False):
            dfs(i, j, color3)
            result3 += 1

print(result3, result2)
