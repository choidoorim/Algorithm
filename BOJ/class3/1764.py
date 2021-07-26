"""
- BOJ 1764
- CDR
- .strip() : 문자열 및 공백을 제거해준다
-  array1과 array2 의 중복된 값을 찾는 방법
1. list(set(array1).intersection(array2))
2. list(set(array1) & set(array2))
- and - 논리연산자, & - 비교연산자 / or - 논리연산자, & 비교연산자
"""
from sys import stdin
n, m = map(int, stdin.readline().split())
n_list = [stdin.readline().strip() for _ in range(n)]
m_list = [stdin.readline().strip() for _ in range(m)]
result_list = sorted(list(set(n_list).intersection(m_list)))

print(len(result_list))
for result in result_list:
    print(result)
