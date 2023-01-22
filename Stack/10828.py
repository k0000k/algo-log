import sys

class my_stack:
    number_stack = []

    def push(self, num):
        self.number_stack.append(num)

    def empty(self):
        if not self.number_stack:
            print(1)
        else:
            print(0)

    def pop(self):
        if not self.number_stack:
            print(-1)
        else:
            print(self.number_stack[-1])
            self.number_stack.pop()
    
    def size(self):
        print(len(self.number_stack))

    def top(self):
        if not self.number_stack:
            print(-1)
        else:
            print(self.number_stack[-1])


cnt = int(input())
num = my_stack()

for i in range(cnt):
    stack_cmd = sys.stdin.readline().rstrip()
    if (stack_cmd[0:4] == "push"):
        x = stack_cmd[5:]
        num.push(x)
    else:
        getattr(num, stack_cmd)()
