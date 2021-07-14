"""
- BOJ 1874
- CDR
"""
from sys import stdin

n = int(stdin.readline())

array = []
operator = []
count = 1
status = True
for _ in range(n):
    num = int(stdin.readline())
    while count <= num:     # 입력 된 숫자보다 count 가 작으면 push
        array.append(count)
        operator.append('+')
        count += 1
    if array[-1] == num:    # 입력 된 숫자가 배열 내 마지막에 존재한다면 pop
        array.pop()
        operator.append('-')
    elif array[-1] != num:   # 배열 내에서 pop 할 수 있는 숫자가 없을 경우
        print('NO')
        status = False
        break

if status:
    for i in operator:
        print(i)
