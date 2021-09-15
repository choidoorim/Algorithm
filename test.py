from itertools import permutations
N, M = map(int, input().split())
# visited = [False] * N
# result = []
#
#
# def solution(depth, n, m):
#     if depth == m:
#         print(result)
#         return
#     for i in range(len(visited)):
#         if not visited[i]:
#             visited[i] = True
#             result.append(i + 1)
#             solution(depth + 1, n, m)
#             visited[i] = False
#             result.pop()
#
#
# solution(0, N, M)

result = permutations(range(1, N + 1), M)
for i in result:
    res = list(map(str, i))
    print(" ".join(res))
