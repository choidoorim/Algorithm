def dfs(graph, v, visited):
    visited[v] = True   # 현재 방문한 node 방문처리
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * 9  # 방문 기록 0 ~ 9
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]  # 0 ~ 9

dfs(graph, 1, visited)
