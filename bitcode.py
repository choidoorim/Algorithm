# from collections import deque
#
#
# def solution(board):
#     answer = 0
#
#     graph = []
#     for i in board:
#         graph.append(list(i))
#     result = []
#
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#
#     def bfs(x, y, new_graph):
#         queue = deque()
#         queue.append((x, y))
#         while queue:
#             x, y = queue.popleft()
#             for i in range(4):
#                 nx = dx[i] + x
#                 ny = dy[i] + y
#                 if nx < 0 or ny < 0 or nx >= len(new_graph) or ny >= len(new_graph):
#                     continue
#                 if new_graph[nx][ny] == 0:
#                     continue
#                 if new_graph[nx][ny] == 1:
#                     new_graph[nx][ny] = new_graph[x][y] + 1
#                     queue.append((nx, ny))
#
#     for i in range(len(graph)):
#         length_graph = graph
#         width_graph = graph
#         for j in range(len(graph)):
#             print(graph[i][j])
#             print(graph[j][i])
#             # print(length_graph)
#             # print(width_graph)
#
#
#     return answer
#
#
# print(solution(["ABBBBC", "AABAAC", "BCDDAC" ,"DCCDDE", "DCCEDE", "DDEEEB"]))
#

def solution(n, capacity, files):
    answer = 0
    while n != 0:
        for i in range(len(files)-1, -1, -1):
            print(files[0], files[i], files)
            if files[0] + files[i] <= capacity:
                answer += 2
                n -= 1
                del files[0]
                del files[i]
                print(files)
                break
            if i == 0:
                answer += 1
                n -= 1
    return answer


print(solution(1, 5, [1, 4, 5]))
