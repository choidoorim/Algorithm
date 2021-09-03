# 1 ~ 99까지는 한수이다, 100부터는 각자리수의 차이가 같으면 한수다.
n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i <= 99:
        cnt += 1
    else:
        num = list(map(int, str(i)))
        if num[0] - num[1] == num[1] - num[2]:
            cnt += 1
print(cnt)
