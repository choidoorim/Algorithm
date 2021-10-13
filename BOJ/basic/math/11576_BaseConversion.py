"""
백준 : 11576
A 진수를 10 진수로 변환한 뒤, 다시 B 진수로 변환.
"""
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
array = list(map(int, input().split()))
total = 0
power = 0
for i in array[::-1]:   # A 진수 10 진수로 변환
    total += (i * (A ** power))
    power += 1

result = []
while total:    # B 진수로 변환
    result.append(str(total % B))
    total //= B

print(' '.join(result[::-1]))
