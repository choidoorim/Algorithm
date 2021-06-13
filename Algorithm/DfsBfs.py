from collections import deque

stack_array = []


def stack_push(data):
    stack_array.append(data)


def stack_pop():
    del stack_array[-1]


# stack
def stack():
    stack_push(1)
    stack_push(2)
    stack_push(3)
    stack_pop()
    stack_push(4)
    print(stack_array)


queue = deque()


def queue_pop():
    del queue[0]


def queue_push(data):
    queue.append(data)


# queue
def queue():
    queue_push(5)
    queue_push(2)
    queue_push(3)
    queue_push(7)
    queue_pop()
    queue_push(1)
    queue_push(4)
    queue_pop()

    queue.reverse()
    a = list(queue)

    print(a)


# 재귀 함수
def recursive_function(i):
    if i == 50:
        print(i, '번째에서 종료합니다.')
        return
    print('재귀 함수를 호출 합니다.')
    recursive_function(i+1)


def factorial(n):   # 수열
    result = 1
    for i in range(1, n+1):     # 1 ~ n까지
        result *= i
    return result


def recursive_factorial(n):
    if n <= 1:
        return 1
    print(recursive_factorial(n-1))
    return n * recursive_factorial(n-1)

INF = 999999999 # 무한의 비용
def ad_matrix():
    graph = [
        [0, 7, 5],
        [7, 0, INF],
        [5, INF, 0]
    ]
    print(graph)


def ad_list(n, m):
    graph = [[] for _ in range(3)]
    graph[0].append((1, 7))
    graph[0].append((2, 5))
    graph[1].append((0, 7))
    graph[2].append((0, 5))
    print(graph[n][m])


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


dfs(graph, 2, visited)
