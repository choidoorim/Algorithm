import sys


def push(number):
    array.append(number)


def pop(arr):
    if not arr:
        print(-1)
    else:
        print(arr[-1])
        del arr[-1]


def size(arr):
    return len(arr)


def empty(arr):
    if arr:
        return 0
    else:
        return 1


def top(arr):
    if not arr:
        return -1
    else:
        return arr[-1]


n = int(sys.stdin.readline())

array = []
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop(array)
    elif command[0] == "size":
        print(size(array))
    elif command[0] == "empty":
        print(empty(array))
    elif command[0] == "top":
        print(top(array))

