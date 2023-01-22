from collections import deque

N = int(input())
temp = list(map(int, input().split()))
ballons = deque((i + 1, temp[i]) for i in range(N))

print(ballons[0][0])
move = ballons.popleft()[1]

while (ballons):
    if (move > 0):
        for i in range(move - 1):
            ballons.append(ballons.popleft())
        print(ballons[0][0])
        move = ballons.popleft()[1]
    else:
        for i in range(abs(move)):
            ballons.appendleft(ballons.pop())
        print(ballons[0][0])
        move = ballons.popleft()[1]
