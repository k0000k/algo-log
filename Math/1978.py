import math

cnt = int(input())
nums = list(map(int, input().split()))
prime = 0

for num in nums:
    if (num == 1):
        continue
    limit = int(math.sqrt(num))
    for i in range(2, limit+1):
        if (num%i == 0):
            break
    else:
        prime += 1

print(prime)
