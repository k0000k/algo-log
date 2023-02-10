import sys, itertools, math

cnt = int(sys.stdin.readline())

for i in range(cnt):
    nums = list(map(int, sys.stdin.readline().split()))
    comb = list(itertools.combinations(nums[1:], 2))

    sum = 0

    for i in comb:
        sum += math.gcd(i[0], i[1])
    
    print(sum)
