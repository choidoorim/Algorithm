N = int(input())


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


cnt = 0
n_factorial = str(factorial(N))
for i in range(len(n_factorial)-1, -1, -1):
    if n_factorial[i] == '0':
        cnt += 1
    else:
        break

print(cnt)
