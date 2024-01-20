n = int(input())
nums = list(map(int, input().split()))

answer = 0
for i in nums:
    if (answer % 3 == i):
        answer += 1

print(answer)