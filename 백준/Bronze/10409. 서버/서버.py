n, T = map(int, input().split())
nums = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += nums[i]
    if (sum > T):
        print(i)
        break
else:
    print(n)
