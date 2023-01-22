from itertools import combinations_with_replacement

cnt = int(input())
cases = []

for i in range(cnt):
    cases.append(int(input()))

for case in cases:
    max_n = 1
    while (True):
        if (max_n * (max_n + 1) / 2 < case):
            max_n += 1
            continue
        else:
            max_n -= 1
            break

    nums = [i for i in range(1, max_n + 1)]
    comb = list(combinations_with_replacement(nums, 3))
    
    for i, j, k in comb:
        if (i * (i + 1) + j * (j + 1) + k * (k + 1) == 2 * case):
            print(1)
            break
    else:
        print(0)
