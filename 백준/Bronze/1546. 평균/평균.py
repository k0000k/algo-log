cnt = int(input())
nums = list(map(int, input().split()))

M = max(nums)
mean = sum(nums) / len(nums)

answer = mean * (100 / M)

print(answer)