from collections import deque

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

maps[x][y] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_count = 0
while True:
    direction -= 1
    if direction < 0:
        direction = 3
    nx = x + dx[direction]
    ny = y + dy[direction]
    if maps[nx][ny] == 0:
        print(maps)
        maps[nx][ny] = 1
        count += 1
        x = nx
        y = ny
        turn_count = 0
    else:
        turn_count += 1
    if turn_count == 4:
        nx = x - dx[direction]
        ny = x - dy[direction]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
            turn_count = 0
        else:
            break

print(count)