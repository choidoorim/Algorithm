# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
INF = 1e9   # 10억
n, m = map(int, input().split())    # 노드와 간선
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a 노드에서 b 노드로 가는 거리인 c


def small_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = small_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

print(distance)