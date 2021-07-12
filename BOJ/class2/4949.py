"""
- BOJ 4949
- CDR
"""
import sys


def check_ps(str_arr):
    array = []
    for i in str_arr:
        if i == '(' or i == '[':
            array.append(i)
        elif i == ')':
            if array and array[-1] == '(':  # 배열이 존재하며 마지막 배열이 맞을 때
                array.pop()
            else:   # 배열이 비어있거나 괄호가 맞지 않을 경우
                return False
        elif i == ']':
            if array and array[-1] == '[':
                array.pop()
            else:
                return False
    if array:
        return False
    elif not array:
        return True


while True:
    string = sys.stdin.readline()
    if string[0] == '.':
        break
    if check_ps(string):
        print('yes')
    elif not check_ps(string):
        print('no')
