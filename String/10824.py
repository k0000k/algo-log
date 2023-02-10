import sys

a, b, c, d = sys.stdin.readline().rstrip().split()
result = int(a + b) + int(c + d)
print(result)
