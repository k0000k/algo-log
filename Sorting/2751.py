import sys

n = int(input())
numbers = [0 for _ in range(n)]

for i in range(n):
    numbers[i] = int(sys.stdin.readline())

numbers.sort()

result = ""
for i in numbers:
    result += str(i)+"\n"
print(result)
