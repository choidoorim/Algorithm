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
    if sum_tree >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)