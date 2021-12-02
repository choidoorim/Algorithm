import sys
# my Code
# n = int(sys.stdin.readline())
#
# array = []
# for i in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     array.append((x, y))
#
# for i in range(n):
#     min_value = i
#     for j in range(i + 1, n):
#         if array[min_value][0] > array[j][0]:
#             min_value = j
#         elif array[min_value][0] == array[j][0]:
#             if array[min_value][1] > array[j][1]:
#                 min_value = j
#     array[i], array[min_value] = array[min_value], array[i]
#
# for i in array:
#     print(i[0], i[1])

# good Code
import sys
input = sys.stdin.readline
N = int(input())
array = []
for _ in range(N):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort(key=lambda x:(x[0],x[1]))
for a, b in array:
    print(a, b)

