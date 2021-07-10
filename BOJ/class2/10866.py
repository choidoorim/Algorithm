"""
- BOJ 10866
- CDR
- 덱은 스택과 큐의 기능이 모두 있는 것.
"""
import sys

n = int(sys.stdin.readline())


def push_front(arr, num):
    arr.reverse()
    arr.append(num)
    arr.reverse()


def push_back(arr, num):
    arr.append(num)


def pop_front(arr):
    if not arr:
        print(-1)
    else:
        print(arr[0])
        del arr[0]


def pop_back(arr):
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
        print(arr[0])


def back(arr):
    if not arr:
        print(-1)
    else:
        print(arr[-1])


array = list()
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == 'push_front':
        push_front(array, command[1])
    elif command[0] == 'push_back':
        push_back(array, command[1])
    elif command[0] == 'pop_front':
        pop_front(array)
    elif command[0] == 'pop_back':
        pop_back(array)
    elif command[0] == 'size':
        size(array)
    elif command[0] == 'empty':
        empty(array)
    elif command[0] == 'front':
        front(array)
    elif command[0] == 'back':
        back(array)
