import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(n)] # dp[i]는 nums[i]를 마지막 값으로 하는 증가 수열중에 가장 긴 것의 길이

for i in range(1, n):
    for j in range(i):
        if (nums[j] < nums[i] and dp[i] < dp[j] + 1):
            dp[i] = dp[j] + 1

print(max(dp))
            
