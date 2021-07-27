import sys
sys.setrecursionlimit(10000)


def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if graph[x][y] == 1:
            graph[x][y] = 2
            # 대각선 포함
            dfs(x - 1, y - 1)
            dfs(x - 1, y)
            dfs(x - 1, y + 1)
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x + 1, y - 1)
            dfs(x + 1, y)
            dfs(x + 1, y + 1)
            return True
    return False


while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w and h) == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                count += 1
    print(count)
