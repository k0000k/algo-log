import sys

cnt = int(sys.stdin.readline())
operation = sys.stdin.readline().rstrip()

operation_dict = {}
operation_stack = []

for i in range(cnt):
    operation_dict[chr(i + 65)] = int(sys.stdin.readline().rstrip())

for i in operation:
    if (i.isalpha()):
        operation_stack.append(operation_dict[i])
    else:
        b = operation_stack.pop()
        a = operation_stack.pop()
        if (i == "+"):
            operation_stack.append(a + b)
        elif (i == "-"):
            operation_stack.append(a - b)
        elif (i == "*"):
            operation_stack.append(a * b)
        elif (i == "/"):
            operation_stack.append(a / b)
print("%.2f"%operation_stack[0])


# 65, isalpha, isdigit, chr
