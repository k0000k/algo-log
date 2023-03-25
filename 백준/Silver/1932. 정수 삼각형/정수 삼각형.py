import sys

N = int(sys.stdin.readline())
dp = [[0 for j in range(N)] for i in range(N)]
nums = []


for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))

dp[0][0] = nums[0][0]
for i in range(N - 1):
    for j in range(i + 1):
        if (dp[i][j] + nums[i + 1][j] > dp[i + 1][j]):
            dp[i + 1][j] = dp[i][j] + nums[i + 1][j]
        if (dp[i][j] + nums[i + 1][j + 1] > dp[i + 1][j + 1]):
            dp[i + 1][j + 1] = dp[i][j] + nums[i + 1][j + 1]
        
print(max(dp[N - 1]))
        