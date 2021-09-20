"""
- BOJ 11725
- CDR
- 부모 노드 배열을 생성해서 노드 그래프에서 부모노드가 없는 노드를 설정해준다.
- DFS, BFS
"""
from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
node = [[] for _ in range(N + 1)]       # 노드 그래프
parent = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def bfs(start):
    q = deque([start])
    while q:
        v = q.popleft()
        for i in node[v]:
            if parent[i] == 0:      # 부모 노드가 없을 경우
                parent[i] = v       # 부모 노드 설정
                q.append(i)


# def dfs(start):
#     for i in node[start]:
#         if parent[i] == 0:
#             parent[i] = start
#             dfs(i)


bfs(1)

for j in range(2, N + 1):
    print(parent[j])

