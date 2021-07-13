"""
- BOJ 7568
- CDR
"""
import sys


def find_bulk_rank(arr, my_size):
    count = 1
    for bulk in arr:
        if bulk[0] > my_size[0] and bulk[1] > my_size[1]:
            count += 1
    return count


n = int(sys.stdin.readline())

array = list()
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

for i in array:
    print(find_bulk_rank(array, i), end=' ')
