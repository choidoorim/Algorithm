"""
- BOJ 10845
- CDR
"""
import sys
n = int(sys.stdin.readline())
array = list()


def push(arr, num):
    arr.reverse()
    arr.append(num)
    arr.reverse()


def pop(arr):
    if not arr:
        print(-1)
    else:
        print(arr[-1])
        del arr[-1]


def size(arr):
    print(len(arr))


def empty(arr):
    if arr:
        print(0)
    else:
        print(1)


def front(arr):
    if not arr:
        print(-1)
    else:
        print(arr[-1])


def back(arr):
    if not arr:
        print(-1)
    else:
        print(arr[0])


for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push':
        push(array, int(command[1]))
    elif command[0] == 'pop':
        pop(array)
    elif command[0] == 'size':
        size(array)
    elif command[0] == 'empty':
        empty(array)
    elif command[0] == 'front':
        front(array)
    elif command[0] == 'back':
        back(array)
