d = [0]*100

def memoization_fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:   # 만약 이미 계산된적이 있다면 재귀함수를 실행시키지 않도록 함.
        return d[x]
    d[x] = memoization_fibo(x - 1) + memoization_fibo(x - 2)
    return d[x]


print(memoization_fibo(4))