from sys import stdin
input = stdin.readline


def decimal(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    num = int(input())
    confirm_flag = False
    a, b = 0, 0
    if num == 0:
        break
    for j in range(2, num + 1):
        a, b = j, num - j
        if decimal(a) and decimal(b):
            confirm_flag = True
            break
    print('{} = {} + {}'.format(num, a, b) if confirm_flag else "Goldbach's conjecture is wrong.")

