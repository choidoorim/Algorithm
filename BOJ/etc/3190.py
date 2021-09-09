from collections import deque
N = int(input())
board = [[0] * N for _ in range(N)]
snake = deque()
snake.append([0, 0])
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1
L = int(input())
direction_change = dict()
for _ in range(L):
    x, c = input().split()
    direction_change[int(x)] = c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
now_dic = 1
time = 0
nx, ny = 0, 0


def direction(n, command):
    if command == 'L':
        return (n - 1) % 4
    else:
        return (n + 1) % 4


while True:
    time += 1
    nx += dx[now_dic]
    ny += dy[now_dic]

    if time in direction_change.keys():     # 방향전환
        now_dic = direction(now_dic, direction_change[time])

    if 0 <= nx < N and 0 <= ny < N:
        if [nx, ny] in snake:
            break
        if board[nx][ny] == 1:  # 사과를 먹었을 경우
            board[nx][ny] = 0
            snake.appendleft([nx, ny])  # 뱀의 길이를 증가
        elif board[nx][ny] == 0:                   # 사과가 없을 경우
            snake.appendleft([nx, ny])  # 뱀의 머리 위치이동
            snake.pop()         # 전 뱀의 머리 위치 삭제
    else:
        break
print(time)
