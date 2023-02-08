from collections import deque
import sys

cnt = int(sys.stdin.readline())

for i in range(cnt):
    N, target = map(int, sys.stdin.readline().split())
    docs = deque(map(int, sys.stdin.readline().split()))
    result = 0

    while (True):
        if (target == 0 and docs[0] == max(docs)):
            docs.popleft()
            result += 1
            break

        elif (docs[0] == max(docs)):
            docs.popleft()
            result += 1
            target -= 1

        else:
            docs.append(docs.popleft())
            if (target == 0):
                target = len(docs) - 1
            else:
                target -= 1
    print(result)


    
