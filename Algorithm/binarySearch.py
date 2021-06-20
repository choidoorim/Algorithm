import sys


def s_search(n, target, array):
    for i in range(len(array)):
        if array[i] == target:
            return i + 1


def sequential_search():
    data = input().split()
    n = int(data[0])
    target = data[1]

    array = input().split()

    print(s_search(n, target, array))


# sequential_search()


def b_search_recursive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return b_search_recursive(array, target, start, mid - 1)
    else:
        return b_search_recursive(array, target, mid + 1, end)


def binary_search_recursive():
    n, target = map(int, input().split())
    array = list(map(int, input().split()))

    result = b_search_recursive(array, target, 0, n - 1)
    if result is None:
        print('원소가 없다.')
    else:
        print(result + 1)


# binary_search_recursive()


def b_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def binary_search():
    n, target = map(int, input().split())
    array = list(map(int, input().split()))

    result = b_search(array, target, 0, n - 1)
    if result is None:
        print('원소가 없다.')
    else:
        print(result + 1)


# 가게 재고
def store_stock():
    n = int(input())
    store = list(map(int, input().split()))
    store.sort()

    # 손님이 부탁한 물품 목록
    m = int(input())
    company = list(map(int, input().split()))
    company.sort()

    for i in company:
        result = b_search(store, i, 0, n - 1)
        if result is None:
            print('no', end=' ')
        else:
            print('yes', end=' ')


# store_stock()

