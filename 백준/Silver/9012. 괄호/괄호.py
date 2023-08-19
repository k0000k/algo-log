import sys

cnt = int(sys.stdin.readline())

for i in range(cnt):
    parenthesis = sys.stdin.readline().rstrip()

    while ("()" in parenthesis):
        start = parenthesis.index("()")
        parenthesis = parenthesis[:start] + parenthesis[start + 2:]
        
    if (parenthesis == ""):
        print("YES")
    else:
        print("NO")

    