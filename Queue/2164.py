from collections import deque
import sys

N = int(sys.stdin.readline())

numbers = deque([i for i in range(1, N + 1)])

while (len(numbers) != 1):
    numbers.popleft()
    numbers.append(numbers.popleft())

print(numbers[0])
