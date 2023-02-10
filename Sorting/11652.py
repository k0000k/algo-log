import sys

cnt = int(sys.stdin.readline())
nums = {}

for i in range(cnt):
    temp = int(sys.stdin.readline())

    if (temp not in nums.keys()):
        nums[temp] = 1
    else:
        nums[temp] += 1

max_num = max(nums.values())
result = []

for i in nums.keys():
    if (nums[i] == max_num):
        result.append(i)
print(min(result))

