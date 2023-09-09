import sys

n = int(sys.stdin.readline().rstrip())
see = []

for i in range(n):
    length = int(sys.stdin.readline().rstrip())

    if (not see):
        see.append(length)
        continue

    while (see and length >= see[-1]):
        see.pop()

    see.append(length)

print(len(see))