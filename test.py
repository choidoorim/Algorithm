n = int(input())

d = [0] * 30001
for i in range(2, n + 1):
    # 현재에서 1을 빼주는 경우
    d[i] = d[i - 1] + 1
    # 현재에서 5, 3, 2로 나누어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    elif i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])
