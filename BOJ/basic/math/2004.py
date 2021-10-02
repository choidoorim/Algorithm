"""
끝자리가 0이라는 것은 2 와 5 의 곱으로 이루어졌을 경우 된다.
2와 5의 짝이 맞아야 1-이 되므로 2의 개수와 5의 개수 중 더 작은것이 10의 개수이다.
"""
n, m = map(int, input().split())


def numCount(div, num):
    cnt = 0
    while num != 0:
        num = num // div
        cnt += num
    return cnt


print(min(numCount(2, n) - numCount(2, m) - numCount(2, n - m), numCount(5, n) - numCount(5, m) - numCount(5, n - m)))
