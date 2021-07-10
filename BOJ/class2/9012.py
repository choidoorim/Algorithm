"""
- BOJ 9012
- CDR
- '('은 stack 에 담고, ')'은 비교하여 뺀다.
- 주어진 모든 괄호를 비교 시, 비교 중간에 배열에 값이 없거나, 비교 후 남아있는 값이 있다면 괄호 충족하지 못한다.
  괄호를 충족하는 경우는 비교가 끝난 후 배열에 값이 존재하지 않아야 한다.
"""
import sys

n = int(sys.stdin.readline())


def push_stack(arr, string):
    arr.reverse()
    arr.append(string)
    arr.reverse()


def pop_stack(arr):
    del arr[-1]


def check_ps(cps):
    array = []
    for i in cps:
        if i == '(':
            push_stack(array, i)
        elif i == ')':
            if not array:   # for 문이 실행되는 도중 배열이 비어있는 경우는 괄호 충족 X
                return False
            else:
                pop_stack(array)
    if not array:   # for 문이 끝났을 때 배열이 비어있으면 괄호 충족
        return True
    elif array:     # for 문이 끝났을 때 배열에 값이 존재한다면 괄호 충족 X
        return False


for _ in range(n):
    ps = sys.stdin.readline().rstrip()
    if check_ps(ps):
        print('YES')
    elif not check_ps(ps):
        print('NO')
    else:
        print('ERR')
