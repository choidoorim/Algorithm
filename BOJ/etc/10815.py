N = int(input())
n_array = list(map(int, input().split()))
M = int(input())
m_array = list(map(int, input().split()))

n_array.sort()


def b_search(array, n, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == n:
            return 1
        elif array[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for target in m_array:
    print(b_search(n_array, target, 0, N - 1), end=' ')
