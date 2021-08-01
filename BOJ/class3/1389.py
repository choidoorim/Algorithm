"""
- BOJ 1389
- CDR
- bfs
- 모든 유저가 케빈 베이컨 게임을 하고 그 중 작은 결과 값을 출력한다
- 참고 https://resilient-923.tistory.com/229
"""
from collections import deque


def bfs(start):
    q = deque()
    visited = [0] * (n + 1)
    q.append(start)
    visited[start] = 1
    while q:
        v = q.popleft()
        for f in graph[v]:
            if not visited[f]:
                visited[f] = visited[v] + 1
                q.append(f)
    return sum(visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n + 1):
    result.append(bfs(i))

print(result.index(min(result)) + 1)
