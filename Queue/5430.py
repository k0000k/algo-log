import sys
from collections import deque

cnt = int(sys.stdin.readline().rstrip())

for i in range(cnt):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    if (n == 0):
        dq = input()
        if ("D" in command):
            print("error")
            continue
        else:
            print("[]")
            continue

    dq = deque(map(int, sys.stdin.readline().rstrip().strip("[]").split(",")))
    result = ""
    reverse = False
    try:
        for i in command:
            if (i == "R"):
                reverse = not reverse
            elif (i == "D"):
                if (reverse == False):
                    dq.popleft()
                else:
                    dq.pop()
    except:
        print("error")
        continue

    if (len(dq) == 0):
        print("[]")
    else:
        if (reverse == True):
            dq.reverse()

        for i in dq:
            result += str(i) + ","
        result = result[:-1]
        print("[" + result + "]")

