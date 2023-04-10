import sys

A, B = map(int, sys.stdin.readline().split())

result = 0
while(B > A):
    if (str(B)[-1] == '1'):
        B = (B - 1) // 10
    elif (B % 2 == 0):
        B = B // 2
    else:
        break
    result += 1

if (B == A):
    print(result + 1)
else:
    print(-1)