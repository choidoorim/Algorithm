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


