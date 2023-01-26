import sys

sentence = sys.stdin.readline().rstrip()
cnt = int(sys.stdin.readline())

stack_left = []
stack_right = []

for i in sentence:
    stack_left.append(i)

for i in range(cnt):
    command = sys.stdin.readline().rstrip()

    if (command[0] == "L" and stack_left):
        stack_right.append(stack_left.pop())

    elif (command[0] == "D" and stack_right):
        stack_left.append(stack_right.pop())

    elif (command[0] == "B" and stack_left):
        stack_left.pop()

    elif (command[0] == "P"):
        stack_left.append(command[-1])

for i in stack_left:
    print(i, end="")

for i in range(len(stack_right) - 1, -1, -1):
    print(stack_right[i], end="")

