cnt, m = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

for i in range(cnt):
    for j in range(i+1, cnt):
        for n in range(j+1, cnt):
            sum = nums[i]+nums[j]+nums[n]
            if (sum <= m and sum > result):
                result = sum
print(result)  
