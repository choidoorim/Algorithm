"""
- BOJ 1920
- CDR
- 이진탐색을 활용해야 한다. 반드시 배열이 정렬되어 있어야 한다.
"""
import sys


def binary_search(num, array, start, end):  # 이진탐색은 반드시 정렬되어 있어야 한다.
    if start > end:
        return 0
    mid = (start+end)//2
    if array[mid] == num:
        return 1
    elif num < array[mid]:
        return binary_search(num, array, start, mid - 1)
    else:
        return binary_search(num, array, mid + 1, end)


def find_num(arr, num):  # 전체 배열을 찾기 때문에 시간초과 오류 발생
    for j in arr:
        if j == num:
            return 1
    return 0


n = int(sys.stdin.readline())
n_array = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))


for i in m_array:
    start = 0
    end = n - 1
    # print(binary_search(i, n_array, start, end))
    print(find_num(n_array, i))