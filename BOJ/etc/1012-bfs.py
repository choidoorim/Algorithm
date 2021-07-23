import sys
from collections import deque

dx = [0, 0, -1, 1]  # 상, 하, 좌, 우
dy = [-1, 1, 0, 0]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        a, b = queue.popleft()
        for j in range(4):
            nx = a + dx[j]
            ny = b + dy[j]
            if nx >= 0 and ny >= 0 and nx < m and ny < n:   # 다음 행선지가 배열안에 들어올 때
                if array[nx][ny] == 1:
                    queue.append((nx, ny))
                    array[nx][ny] = 0


t = int(input())
for _ in range(t):
    count = 0
    m, n, k = map(int, sys.stdin.readline().split())
    array = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        array[x][y] = 1
    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
