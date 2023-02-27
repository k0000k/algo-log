import sys

def check_sum(standard, moneys):
    sum = 0
    for i in moneys:
        if (i >= standard):
            sum += standard
        else:
            sum += i
    return sum

cnt = int(sys.stdin.readline())
moneys = list(map(int, sys.stdin.readline().split()))
max_money = int(sys.stdin.readline())

if (sum(moneys) <= max_money):
    print(max(moneys))
    sys.exit()


left = min(moneys)
right = max(moneys)
mid = (left + right) // 2

if (check_sum(left, moneys) > max_money):
    left = 0

while (True):
    sum = check_sum(mid, moneys)
    if (sum == max_money):
        print(mid)
        break
    if (mid == left):
        rigth_sum = check_sum(right, moneys)
        if (rigth_sum <= max_money):
            print(right)
        else:
            print(mid)
        break
    elif (sum > max_money):
        right = mid
        mid = (left + right) // 2
    else:
        left = mid
        mid = (left + right) // 2

