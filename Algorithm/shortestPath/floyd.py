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

print(graph)
