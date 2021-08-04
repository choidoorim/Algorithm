"""
- Programmers - 직사각형 별찍기
- CDR
"""


a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*' * a)
