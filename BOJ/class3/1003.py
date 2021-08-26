"""
- BOJ 1003
- CDR
- 0과 1의 호출되는 수의 공통점은 아래와 같이 피보나치 수의 결과와 비슷하다는 점을 확인할 수 있다.
0: 1 0 1 1 2 3 ..
1: 0 1 1 2 3 5 ..
"""
t = int(input())


def fibo(n):
    d = [0] * 41
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]


for _ in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
    else:
        print(fibo(n - 1), fibo(n))

