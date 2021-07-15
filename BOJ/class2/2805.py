"""
- BOJ 2805
- CDR
- 자르기 문제는 이분탐색을 활용하자, 이분 탐색을 활용하지 않을 경우 시간초과 발생할 가능성이 높아
"""
from sys import stdin


def time_out():
    n, m = map(int, stdin.readline().split())
    trees = list(map(int, stdin.readline().split()))

    cut = max(trees)

    while True:
        sum_tree = 0
        for tree in trees:
            if tree >= cut:
                sum_tree += tree - cut
        if sum_tree >= m:
            print(cut)
            break
        cut -= 1


def binary_search_timeout():
    n, m = map(int, stdin.readline().split())
    trees = list(map(int, stdin.readline().split()))

    start, end = 1, max(trees)

    while True:
        mid = (start + end) // 2    # 절단기의 길이
        sum_tree = 0
        for tree in trees:
            if tree >= mid:  # 나무의 길이가 절단기의 길이와 같거나 클 경우에만 컷팅을 함
                sum_tree += tree - mid
        if sum_tree == m:
            print(mid)
            break
        elif sum_tree < m:
            end = mid - 1
        else:
            start = mid + 1


def binary_search():
    from sys import stdin
    n, m = map(int, stdin.readline().split())
    trees = list(map(int, stdin.readline().split()))

    start, end = 1, max(trees)

    while start <= end:
        mid = (start + end) // 2
        sum_tree = 0
        for tree in trees:
            if tree >= mid:
                sum_tree += tree - mid
        if sum_tree < m:
            end = mid - 1
        else:
            start = mid + 1
    print(end)


def success(trees, num):
    start, end = 1, max(trees)

    while start <= end:
        mid = (start + end) // 2
        sum_tree = 0
        for tree in trees:
            if tree >= mid:
                sum_tree += tree - mid
        if sum_tree >= num:
            start = mid + 1
        else:
            end = mid - 1
    return end


n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

print(success(trees, m))
