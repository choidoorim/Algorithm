"""
- BOJ 1874
- CDR
"""
"""
from sys import stdin
n = int(stdin.readline())

count = 1
array = []
result = []
status = True
for _ in range(n):
    num = int(stdin.readline())
    while count <= num:
        array.append(count)
        result.append('+')
        count += 1
    if array[-1] == num:
        result.append('-')
        array.pop()
    elif array != num:
        print('NO')
        status = False
        break

if status:
    for i in result:
        print(i)
"""

import sys
input = sys.stdin.readline

n = int(input())
array = []  # 숫자
calc = []   # 연산 결과
cnt = 1     # 1 ~ n 까지 수열을 만들기 위한 수
answer_flag = True  # 정답 여부

for _ in range(n):
    num = int(input())
    while cnt <= num:
        array.append(cnt)
        cnt += 1
        calc.append('+')
    if array[-1] == num:
        array.pop()
        calc.append('-')
    else:
        answer_flag = False
        break

if answer_flag:
    for c in calc:
        print(c)
else:
    print('NO')
