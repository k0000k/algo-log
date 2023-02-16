import sys
from collections import deque

def bfs(maze, road, N, M):
    road[0][0] = 1
    dq = deque()
    dq.appendleft((0, 0))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while (dq):
        v = dq.pop()
        for i in range(4):
            next_x = v[0] + dx[i]
            next_y = v[1] + dy[i]
            if (0 <= next_x <= N - 1 and 0 <= next_y <= M - 1):
                if (maze[next_x][next_y] == "1" and road[next_x][next_y] == 0):
                    road[next_x][next_y] = road[v[0]][v[1]] + 1
                    dq.appendleft((next_x, next_y))


N, M = map(int, sys.stdin.readline().split())
maze = []
road = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    temp = sys.stdin.readline().rstrip()
    maze.append(temp)

bfs(maze, road, N, M)

print(road[N - 1][M - 1])
    
