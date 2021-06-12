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


def dfs(graph, v, visited):
    visited[v] = True   # 현재 노드 방문 처리
    print(v, end=' ')
    print(visited)
    for i in graph[v]:  # 현재 노드와 연결되어 있는 나머지 노드들 확인
        if not visited[i]:  # 방문처리가 되어 있지 않는 노드들만 확인, 더 이상 방문처리를 할 필요가 없을 경우 재귀함수가 호출되지 않음.
            dfs(graph, i, visited)


dfs(graph, 1, visited)
