import sys

N, B = sys.stdin.readline().rstrip().split()
B = int(B)

result = 0
idx = 0
for i in range(len(N) - 1, -1, -1):

    if (N[i].isdigit()):
        result = result + (B ** idx) * int(N[i])
        idx += 1
    else:
        result = result + (B ** idx) * (ord(N[i]) - 55)
        idx += 1
    
print(result)

