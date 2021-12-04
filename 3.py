# bfs 문제
from collections import deque


def solution(v):
    answer = 0
    # v[y좌표][x좌표]

    h = len(v)   # 높이
    w = len(v[0])   # 넓이
    result = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def bfs(y, x):
        q = deque()
        q.append((x, y))
        cnt = 0
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = dx[k] + x
                ny = dy[k] + y
                if 0 <= nx < w and 0 <= ny < h:
                    if v[ny][nx] == 1:
                        q.append((nx, ny))
                        v[ny][nx] = 0
                        cnt += 1
        result.append(cnt)

    for i in range(h):  # y
        for j in range(w):  # x
            if v[i][j] == 1:
                bfs(i, j)
                answer += 1
    return [answer, max(result)]


print(solution([[1,1,1231232,1,1],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,1,1],[1,0,1,1,1]]))