from collections import deque

N = int(input())
apple_cnt = int(input())

board = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(apple_cnt):
    x, y = map(int, input().split())
    board[x][y] = 2

rotations_times = []
rotations_directions = []

for i in range(int(input())):
    a, b = list(input().split())
    rotations_times.append(int(a))
    rotations_directions.append(b)

body = deque()
body.append([1, 1])
timer = 0
move_x = [0, 1, 0, -1] # 처음 방향부터 시계방향
move_y = [1, 0, -1, 0]
move_idx = 0

while (True):

    temp = [body[0][0] + move_x[move_idx], body[0][1] + move_y[move_idx]]

    # 벽 충돌 체크
    if (temp[0] > N or temp[0] == 0 or temp[1] > N or temp[1] == 0):
        break

    # 자신의 몸과 충돌 체크
    if (temp in body):
        break
    else:
        body.appendleft(temp)

    #사과 체크
    if (board[temp[0]][temp[1]] == 2):
        board[temp[0]][temp[1]] = 0
    else:
        body.pop()

    timer += 1

    # 방향 바꾸기
    if (timer in rotations_times):
        if (rotations_directions[rotations_times.index(timer)] == "D"):
            move_idx += 1
        else:
            move_idx -= 1
        if (move_idx == -1):
            move_idx = 3
        elif (move_idx == 4):
            move_idx = 0

print(timer + 1)
