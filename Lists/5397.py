cnt = int(input())

for i in range(cnt):
    command = input()
    pw = ""
    stack_left = []
    stack_right = []

    for j in command:
        if (j == "<"):
            if (not stack_left):
                continue
            stack_right.append(stack_left.pop())

        elif (j == ">"):
            if (not stack_right):
                continue
            stack_left.append(stack_right.pop())

        elif (j == "-"):
            if (not stack_left):
                continue
            stack_left.pop()

        else:
            stack_left.append(j)
    
    for i in stack_left:
        print(i, end="")

    for i in range(len(stack_right) - 1, -1, -1):
        print(stack_right[i], end="")
    print()
