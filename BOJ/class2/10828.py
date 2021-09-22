"""
- BOJ 10828
- CDR
- 후입선출
"""
from sys import stdin
input = stdin.readline

N = int(input())

stack = []


def push(num):
    stack.append(num)


def pop():
    print(stack.pop() if stack else -1)


def size():
    print(len(stack))


def empty():
    print(0 if stack else 1)


def top():
    print(stack[-1] if stack else -1)


for _ in range(N):
    command = input().split()
    if command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'top':
        top()
    else:
        push(int(command[1]))

"""
# fst
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
"""


