"""
- BOJ 7576
- CDR
- bfs 를 활용하는 문제
"""
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if (0 <= nx < n) and (0 <= ny < m):
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))


m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 익은 토마토가 있을 경우 queue 에 담기
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            queue.append((i, j))

bfs()   # bfs 실행

print_flag = True   # 출력 Flag
max_num = 0
for mp in maps:
    max_num = max(max(mp), max_num)
    if 0 in mp:
        print_flag = False
        break

# 최대 토마토수가 아닌 최소 일수를 계산하기 위한 것이기 때문에 최대 값에서 -1을 한다. 일수는 0일부터 시작이기 때문에.
if print_flag:
    print(max_num - 1)
else:
    print(-1)
