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
    recursive_function(i + 1)


def factorial(n):  # 수열
    result = 1
    for i in range(1, n + 1):  # 1 ~ n까지
        result *= i
    return result


def recursive_factorial(n):
    if n <= 1:
        return 1
    print(recursive_factorial(n - 1))
    return n * recursive_factorial(n - 1)


INF = 999999999  # 무한의 비용


def ad_matrix():
    graph = [
        [0, 7, 5],
        [7, 0, INF],
        [5, INF, 0]
    ]
    print(graph)


def ad_list():
    graph = [[] for _ in range(3)]
    graph[0].append((1, 7))
    graph[0].append((2, 5))
    graph[1].append((0, 7))
    graph[2].append((0, 5))
    print(graph)


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
    visited[v] = True  # 현재 노드 방문 처리
    print(v, end=' ')
    for i in graph[v]:  # 현재 노드와 연결되어 있는 나머지 노드들 확인
        if not visited[i]:  # 방문처리가 되어 있지 않는 노드들만 확인, 더 이상 방문처리를 할 필요가 없을 경우 재귀함수가 호출되지 않음.
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 미로 탈출
def bfs_mirror(x, y):
    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx, ny)
            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 기존 범위를 벗어나는 경우
                continue
            if graph[nx][ny] == 0:  # 몬스터가 있는 경우
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


# 음료수 얼려먹기
def dfs_ice(x, y):
    if x < 0 or y < 0 or x >= n_ice or y >= m_ice:
        return False
    if graph_ice[x][y] == 0:
        graph_ice[x][y] = 1
        dfs_ice(x - 1, y)
        dfs_ice(x, y - 1)
        dfs_ice(x + 1, y)
        dfs_ice(x, y + 1)
        return True
    return False


def ice():
    global n_ice, m_ice, graph_ice
    n_ice, m_ice = map(int, input().split())

    graph_ice = []
    for i in range(n_ice):
        graph_ice.append(list(map(int, input().split())))

    count = 0
    for i in range(n_ice):
        for j in range(m_ice):
            if dfs_ice(i, j):
                count += 1
    print(count)


ice()
# print(bfs_mirror(0, 0))
# dfs(graph, 1, visited)
# bfs(graph, 1, visited)
