import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    n = int(sys.stdin.readline())
    cloths = {}
    for j in range(n):
        name, kind = sys.stdin.readline().rstrip().split()
        if kind in cloths:
            cloths[kind] += 1
        else:
            cloths[kind] = 1
    
    result = 1
    for j in list(cloths.keys()):
        result *= (cloths[j] + 1)
    
    print(result - 1)