"""
- BOJ 1181
- CDR
"""
array = []
for _ in range(int(input())):
    array.append(input())
array = list(set(array))
array.sort(key=lambda x:(len(x), x))    # 1차 길이로 정렬, 2차 사전 순으로 정렬
for i in array:
    print(i)
