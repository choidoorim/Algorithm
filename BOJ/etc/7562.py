from collections import deque
t = int(input())


dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs(x, y, a, b):
    array[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if x == a and y == b:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] == 0:
                    array[nx][ny] = array[x][y] + 1
                    q.append((nx, ny))


for _ in range(t):
    n = int(input())
    array = [[0] * n for _ in range(n)]
    from_a, from_b = map(int, input().split())
    to_a, to_b = map(int, input().split())
    bfs(from_a, from_b, to_a, to_b)
    print(array[to_a][to_b] - 1)    # 현재 도착했을 때 6 이기 때문에 해당 위치까지 도착하기 위해서는 -1 한 5 입니다.
