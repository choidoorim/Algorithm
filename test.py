from collections import deque


def solution(v):
    cnt = 0
    max_area = []
    m = len(v[0])
    n = len(v)

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def bfs(a, b):
        q = deque()
        q.append((a, b))
        area_cnt = 0
        while q:
            a, b = q.popleft()
            for k in range(4):
                nx = a + dx[k]
                ny = b + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if v[nx][ny] == 1:
                        q.append((nx, ny))
                        v[nx][ny] = 0
                        area_cnt += 1
        max_area.append(area_cnt)

    for i in range(n):
        for j in range(m):
            if v[i][j] == 1:
                bfs(i, j)
                cnt += 1
    return [cnt, max(max_area)]


print(solution([[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,1,1],[1,0,1,1,1]]))