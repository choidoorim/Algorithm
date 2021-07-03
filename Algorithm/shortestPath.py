import sys
input = sys.stdin.readline  # input을 빠르게 동작 시켜주는 코드
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():    # 가장 작은 노트 값을 찾아준다.
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:  # 방문하지 않았고 거리가 최소 보다 작을 때
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n - 1):
        now = get_smallest_node()   # 현재 값
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)


for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

