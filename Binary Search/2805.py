import sys

def check_sum(standard, trees):
    sum = 0
    for i in trees:
        if (i > standard):
            sum = sum + (i - standard)
    return sum

cnt_of_trees, require_tree = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left = min(trees)
right = max(trees)

if (check_sum(left, trees) < require_tree):
    left = 0

mid = (left + right) // 2

while(True):
    sum = check_sum(mid, trees)
    if (sum == require_tree):
        print(mid)
        break
    if (left == mid):
        right_sum = check_sum(right, trees)
        if (right_sum >= require_tree):
            print(right)
        else:
            print(mid)
        break
    if (sum < require_tree):
        right = mid
        mid = (left + right) // 2
    elif (sum > require_tree):
        left = mid
        mid = (left + right) // 2
