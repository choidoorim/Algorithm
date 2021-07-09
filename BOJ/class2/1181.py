"""
- BOJ 1181
- CDR
"""
import sys
n = int(sys.stdin.readline())

array = list()
for _ in range(n):
    array.append(sys.stdin.readline().rstrip())

array = list(set(array))    # 중복 제거

array.sort(key=lambda x: (len(x), x))
# 길이 우선적으로 정렬, 그 후 사전 순으로 정렬
# 그냥 array.sort를 하면 사전 순으로 정렬이 된다.

for i in array:
    print(i)
