"""
- BOJ 2606
- CDR
"""
from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):  # graph 만들기
    a, b = map(int, stdin.readline().split())
    # ex. 1 - 2 는 node 1 과 node 2 에 모두 엮여있는 것으로 graph 에 둘다 넣어줘야 한다
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0


def dfs(graph, start, visited):
    global count
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1


dfs(graph, 1, visited)
print(count)
