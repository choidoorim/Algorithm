"""
- BOJ 1874
- CDR
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
