# 1
# def solution(id_list, report, k):
#     answer = []
#     my_report = {}
#     report_cnt = {}
#     report_result = {}
#     for ID in id_list:    # 초기화
#         my_report[ID] = []
#         report_cnt[ID] = 0
#         report_result[ID] = False
#     for i in report:
#         a, b = i.split()
#         if b not in my_report[a]:
#             my_report[a].append(b)
#             report_cnt[b] += 1
#     for j in report_cnt:
#         if report_cnt[j] >= k:
#             report_result[j] = True
#     for l in my_report:
#         cnt = 0
#         for n in my_report[l]:
#             if report_result[n]:
#                 cnt += 1
#         answer.append(cnt)
#     return answer
# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

# 2
# def solution(n, k):
#     cnt = 0
#
#     def map_num(num, q):
#         result = ''
#         while num > 0:
#             num, mod = divmod(num, q)
#             result += str(mod)
#         return result[::-1]
#
#     n = map_num(n, k)
#     arr = n.split('0')
#
#     def prime_num(num):
#         if num == 1:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     for i in arr:
#         if i and prime_num(int(i)):
#             cnt += 1
#
#     return cnt
#
#
# print(solution(110011, 10))

# 6 : 효율성 테스트 X
# def solution(board, skill):
#     answer = 0
#
#     def order(tp, r1, c1, r2, c2, degree, cnt):
#         if tp == 1:
#             degree = degree*(-1)
#         for i in range(r1, r2 + 1):
#             for j in range(c1, c2 + 1):
#                 board[i][j] += degree
#
#     for sk in skill:
#         order(sk[0], sk[1], sk[2], sk[3], sk[4], sk[5], answer)
#
#     for bd in board:
#         for k in bd:
#             if k > 0:
#                 answer += 1
#     return answer
#
#
# print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

# 5 - 이진탐색 트리 문제
def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return answer


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
