import sys
input = sys.stdin.readline


def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())
n_array = list(map(int, input().split()))
M = int(input())
m_array = list(map(int, input().split()))
n_array.sort()  # 이분탐색은 정렬이 되어 있어야 한다.
for num in m_array:
    print(1 if binary_search(n_array, 0, N - 1, num) else 0)
