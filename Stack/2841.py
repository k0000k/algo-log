import sys

stack = [[] for i in range(6)]

N, P = map(int, sys.stdin.readline().split())
result = 0

for i in range(N):
    string_num, flat_num = map(int, sys.stdin.readline().split())

    while (True):
        if (not stack[string_num - 1]):
            stack[string_num - 1].append(flat_num)
            result += 1
            break
        elif (stack[string_num - 1][len(stack[string_num - 1]) - 1] > flat_num):
            stack[string_num - 1].pop()
            result += 1
            continue
        elif (stack[string_num - 1][len(stack[string_num - 1]) - 1] == flat_num):
            break
        else:
            stack[string_num - 1].append(flat_num)
            result += 1
            break

print(result)
