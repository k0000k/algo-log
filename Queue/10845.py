import sys

class my_queue:
    number_queue = []

    def push(self, num):
        self.number_queue.append(num)

    def empty(self):
        if not self.number_queue:
            print(1)
        else:
            print(0)

    def pop(self):
        if not self.number_queue:
            print(-1)
        else:
            print(self.number_queue[0])
            del self.number_queue[0]
    
    def size(self):
        print(len(self.number_queue))

    def front(self):
        if not self.number_queue:
            print(-1)
        else:
            print(self.number_queue[0])
    
    def back(self):
        if not self.number_queue:
            print(-1)
        else:
            print(self.number_queue[-1])


cnt = int(input())
num = my_queue()

for i in range(cnt):
    queue_cmd = sys.stdin.readline().rstrip()
    if (queue_cmd[0:4] == "push"):
        x = queue_cmd[5:]
        num.push(x)
    else:
        getattr(num, queue_cmd)()
