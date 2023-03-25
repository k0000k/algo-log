import sys

N = int(sys.stdin.readline())
dp = [[-1, -1, -1] for j in range(N)]
costs = []
idx = [0, 1, 2]

for i in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))

dp[0] = costs[0]
for i in range(N - 1):
    for j in range(3):
        for k in range(3):
            if (j == k):
                continue
            if (dp[i + 1][k] == -1):
                dp[i + 1][k] = dp[i][j] + costs[i + 1][k]
            elif (dp[i][j] + costs[i + 1][k] < dp[i + 1][k]):
                dp[i + 1][k] = dp[i][j] + costs[i + 1][k]

print(min(dp[N - 1]))
