import sys
from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for k in range(8):
            nx = dx[k] + a
            ny = dy[k] + b
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:  # 다음 위치가 1일 경우
                graph[nx][ny] = 0
                queue.append((nx, ny))


while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w and h) == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
