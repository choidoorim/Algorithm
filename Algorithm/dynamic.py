def fibo_recursive(x):
    if x == 1 or x == 2:
        return 1
    return fibo_recursive(x - 1) + fibo_recursive(x - 2)


# print(fibo_recursive(4))


d = [0]*100


def memoization_fibo_recursive(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:   # 만약 이미 계산된적이 있다면 재귀함수를 실행시키지 않도록 함.
        return d[x]
    d[x] = memoization_fibo_recursive(x - 1) + memoization_fibo_recursive(x - 2)
    return d[x]


# print(memoization_fibo_recursive(4))


def memoization_fibo():
    n = int(input())
    array = [0] * 100
    array[1] = 1
    array[2] = 1

    for i in range(3, n + 1):   # range(n) -> n - 1까지
        array[i] = array[i-1] + array[i-2]

    print(array[n])


memoization_fibo()
