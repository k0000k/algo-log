import sys

def check_seg(standard, lines):
    sum = 0
    for i in lines:
        sum = sum + (i // standard)
    return sum

K, N = map(int, sys.stdin.readline().split())
lines = []

for i in range(K):
    lines.append(int(sys.stdin.readline()))

left = 1
right = max(lines)
mid = (left + right) // 2

while (True):
    sum = check_seg(mid, lines)
    if (mid == left):
        right_sum = check_seg(right, lines)
        if (right_sum >= N):
            print(right)
        else:
            print(mid)
        break
    if (sum >= N):
        left = mid
        mid = (left + right) // 2
    else:
        right = mid
        mid = (left + right) // 2
    
