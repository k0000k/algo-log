import sys

cnt = int(sys.stdin.readline())
result = 0

for i in range(cnt):
    AB_stack = []
    word = sys.stdin.readline().rstrip()

    for i in word:
        if (not AB_stack):    
            AB_stack.append(i)
        elif (AB_stack[len(AB_stack) - 1] == i):
            AB_stack.pop()
        else:
            AB_stack.append(i)
    
    if (not AB_stack):
        result += 1

print(result)
        
