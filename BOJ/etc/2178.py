from collections import deque
import sys


def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and mirror[nx][ny] == 1:
                q.append((nx, ny))
                mirror[nx][ny] = mirror[x][y] + 1


input = sys.stdin.readline
n, m = map(int, input().split())
mirror = [list(map(int, input().rstrip())) for _ in range(n)]

bfs(0, 0)
print(mirror[n - 1][m - 1])
