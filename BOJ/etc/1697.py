from collections import deque


def bfs(now, goal):
    q = deque()
    q.append(now)
    while q:
        x = q.popleft()
        if x == goal:
            return arr[x]
        else:
            for nx in (x - 1, x + 1, x * 2):
                if 0 <= nx <= MAX and not arr[nx]:
                    arr[nx] = arr[x] + 1
                    q.append(nx)


n, k = map(int, input().split())
MAX = 10 ** 5
arr = [0] * (MAX + 1)
print(bfs(n, k))
