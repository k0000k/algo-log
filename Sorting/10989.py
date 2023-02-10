import sys

cnt = int(input())
nums = [0 for i in range(10001)]

for i in range(cnt):
    num = int(sys.stdin.readline())
    nums[num] += 1

for i in range(1, 10001):
    for j in range(nums[i]):
        print(i)
