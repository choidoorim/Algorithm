from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if field[nx][ny] == 1:
                    q.append((nx, ny))
                    field[nx][ny] = 0


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    cnt = 0
    field = [[0] * n for i in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
