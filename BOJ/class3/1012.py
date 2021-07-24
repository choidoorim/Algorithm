import sys
from collections import deque


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0


t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * n for _ in range(m)]
    count = 0
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
