from sys import stdin
t = int(stdin.readline())
if t % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = t // 300                # 초를 300 으로 나눈 값
    b = (t % 300) // 60         # 위의 나머지 값을 60으로 나눈 값
    c = ((t % 300) % 60) // 10  # 위의 나머지 값을 10으로 나눈 값
    print(a, b, c)
