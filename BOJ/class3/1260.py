from sys import stdin
from collections import deque


def dfs(graph, start, visited):
    visited[start] = True
    dfs_result.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        start = queue.popleft()
        bfs_result.append(start)
        for j in graph[start]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)


n, m, v = map(int, stdin.readline().split())
dfs_result = []
bfs_result = []
graph = [[] * n for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    # 작은 것 부터 방문해야되기 때문에 정렬 진행

for i in range(len(graph)):
    graph[i].sort()
print(graph)
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs(graph, v, visited_dfs)
bfs(graph, v, visited_bfs)

for dfs in dfs_result:
    print(dfs, end=' ')
print()
for bfs in bfs_result:
    print(bfs, end=' ')
