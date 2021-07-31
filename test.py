from collections import deque
def bfs():
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        now = queue.popleft()
        for i in range(4):
            nx = now[0] + direction[i][0]
            ny = now[1] + direction[i][1]
            if(0 <= nx < N) and (0 <= ny < M):
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[now[0]][now[1]] + 1 # 현재 요소 값에서 +1
                    queue.append((nx, ny))

M, N = map(int, input().split())
queue = deque()
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split()))) # 값이 1인 요소들을 큐에 다 담기(동시 진행을 위한)
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))


bfs()
print(tomato)