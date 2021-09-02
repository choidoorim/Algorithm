import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(1, n):   # 전 집과 같은 색을 제회한 나머지의 최솟값을 찾아 더해준다.
    graph[i][0] += min(graph[i - 1][1], graph[i - 1][2])
    graph[i][1] += min(graph[i - 1][0], graph[i - 1][2])
    graph[i][2] += min(graph[i - 1][0], graph[i - 1][1])
print(min(graph[n - 1]))
