N = int(input())
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for m in money:
    if N <= 0:
        break
    if N // m > 0:
        cnt += N // m
        N = N % m
print(cnt)
