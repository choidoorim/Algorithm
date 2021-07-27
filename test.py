import heapq
INF = 1e9   # 10억
n, m = map(int, input().split())    # 노드와 간선의 수
start_node = int(input())
graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 처리 된 node 일 경우 무시
        if dist > distance[now]:
            continue
        for grp in graph[now]:
            cost = dist + grp[1]
            if distance[grp[0]] > cost:
                distance[grp[0]] = cost
                heapq.heappush(q, (cost, grp[0]))


dijkstra(start_node)

print(distance)
