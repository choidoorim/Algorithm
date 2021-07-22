from sys import stdin
n, m = map(int, stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:  # 현재 위치가 범위에서 벗어날 경우
        return False
    if graph[x][y] == 0:    # 방문하지 않았을 경우
        graph[x][y] = 1     # 방문처리 후 상, 하, 좌, 우를 탐색
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
