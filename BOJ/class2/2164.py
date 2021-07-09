"""
- BOJ 2164
- CDR
"""
import sys
from collections import deque
n = int(sys.stdin.readline())

array = deque()
for i in range(1, n + 1):
    array.append(i)


def push(arr):
    push_num = arr[0]
    del arr[0]
    arr.append(push_num)


def pop(arr):
    del arr[0]


while len(array) > 1:
    pop(array)
    push(array)

print(array[0])
