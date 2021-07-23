"""
- BOJ 1012
- CDR
- DFS 는 RECURSION ERROR 가 발생
- https://fullmoon1344.tistory.com/85 -> limit 으로 해결하였다하셔서 참고하여 해결
"""
import sys
sys.setrecursionlimit(10000)    # runtime Error 를 방지하기 위해 사용


def dfs(a, b):
    if a < 0 or b < 0 or a >= m or b >= n:
        return False
    if array[a][b] == 1:
        array[a][b] = 0
        dfs(a - 1, b)
        dfs(a + 1, b)
        dfs(a, b - 1)
        dfs(a, b + 1)
        return True
    return False


t = int(input())
for _ in range(t):
    count = 0
    m, n, k = map(int, sys.stdin.readline().split())
    array = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        array[x][y] = 1
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                count += 1
    print(count)
