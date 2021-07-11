"""
- BOJ 1436
- CDR
- 브루트포스 알고리즘: 모든 경우를 찾는 알고리즘
- 666부터 수를 1씩 증가시키면서 666이라는 숫자가 포함될 때마다 count 를 증가시킨다.
"""
import sys
n = int(sys.stdin.readline())
movie = 666

count = 0

while True:
    if '666' in str(movie):
        count += 1
    if count == n:
        print(movie)
        break
    movie += 1
