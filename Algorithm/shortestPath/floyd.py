"""
최단 경로를 모두 구해야 하는 경우에 사용할 수 있는 알고리즘
"""
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
INF = int(1e9)

n = int(input())    # 노드
m = int(input())    # 간선

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신은 0으로 초기화
for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0


for _ in range(m):
    # a 에서 b 로가는 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ')
    print()
