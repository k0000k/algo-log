import sys
from collections import deque

cnt = int(input())
dq = deque()

for i in range(cnt):
    command = sys.stdin.readline().rstrip()

    if (command[0:4] == "push"):
        if (command[5] == "f"):
            X = int(command[11:])
            dq.append(X)
        else:
            X = int(command[10:])
            dq.appendleft(X)
    elif (command == "pop_front"):
        if (len(dq) == 0):
            print(-1)
        else:
            print(dq.pop())
    elif (command == "pop_back"):
        if (len(dq) == 0):
            print(-1)
        else:
            print(dq.popleft())
    elif (command == "size"):
        print(len(dq))
    elif (command == "empty"):
        if (len(dq) == 0):
            print(1)
        else:
            print(0)
    elif (command == "front"):
        if (len(dq) == 0):
            print(-1)
        else:
            print(dq[-1])
    elif (command == "back"):
        if (len(dq) == 0):
            print(-1)
        else:
            print(dq[0])
