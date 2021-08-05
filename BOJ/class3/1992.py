"""
- BOJ 1992
- CDR
"""
import sys
input = sys.stdin.readline

num = int(input())
array = [list(map(int, input().rstrip())) for _ in range(num)]


def solution(x, y, n):
    # x, y : x 사분면의 첫번째 좌표
    # n : x 사분면의 크기
    check = array[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != array[i][j]:
                n //= 2     # 8 영상의 크기를 4등분 했을 때 1개 당 크기는 4 이다
                print('(', end='')
                solution(x, y, n)  # 1 사분면
                solution(x, y + n, n)   # 2사분면
                solution(x + n, y, n)   # 3사분면
                solution(x + n, y + n, n)    # 4사분면
                print(')', end='')
                return
    if check == 0:
        print(0, end='')
    else:
        print(1, end='')


solution(0, 0, num)
