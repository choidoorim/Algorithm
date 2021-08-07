"""
- Programmers - 제일 작은 수 제거
- CDR
"""


def solution(arr):
    min_num = min(arr)
    del arr[arr.index(min_num)]     # 배열의 제일 작은 수의 index 를 찾아 제거
    if not arr:
        return [-1]
    return arr


print(solution([10]))
