import sys

def dfs(i, j, city, result):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    city[i][j] = 0
    result += 1

    for a in range(4):
        if (0 <= i + dx[a] <= len(city) - 1 and 0 <= j + dy[a] <= len(city) - 1):
            if (city[i + dx[a]][j + dy[a]]):
                result = dfs(i + dx[a], j + dy[a], city, result)
    return result

cnt = int(sys.stdin.readline())
city = [[0 for i in range(cnt)] for j in range(cnt)]
results = []

for i in range(cnt):
    temp = sys.stdin.readline().rstrip()
    for j in range(cnt):
        if (temp[j] == "1"):
            city[i][j] = 1

for i in range(cnt):
    for j in range(cnt):
        if (city[i][j] == 1):
            result = 0
            result = dfs(i, j, city, result)
            results.append(result)

results.sort()
print(len(results))

for i in results:
    print(i)
