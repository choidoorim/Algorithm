"""
- 백준: 1010
- 조합 공식 사용
    - n 개의 조합에서 k 개를 뽑는 경우: n!//(k!*(n-k)!)
"""
from math import factorial

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(n)*factorial(m-n)))
