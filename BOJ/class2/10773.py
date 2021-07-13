"""
- BOJ 10773
- CDR
"""
import sys

k = int(sys.stdin.readline())

array = list()
for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        del array[-1]
    else:
        array.append(num)

print(sum(array))
