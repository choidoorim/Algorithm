def fibo(x):
    if x == 1:
        return 1
    return x + fibo(x - 1)


print(fibo(3))

