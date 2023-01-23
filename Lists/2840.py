from collections import deque

N, K = map(int, input().split())
dq = deque(["?" for i in range(N)])

for i in range(K):
    S, char = input().split()

    for i in range(int(S)):
        dq.appendleft(dq.pop())
    
    if (dq[0] == "?" and char not in dq):
        dq[0] = char
    elif (dq[0] == char):
        continue
    else:
        print("!")
        exit()

for i in dq:
    print(i, end="")
