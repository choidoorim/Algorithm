def my_code():
    a, b, v = map(int, input().split())
    high = 0
    count = 0

    while True:
        high += a
        if high >= v:
            print(count)
            break
        high -= b
        count += 1

    print(count)
# 시간 초과 발생


# 시간 초과 때문에 while 을 사용하지 않고 한 번에 일수가 계산되어야 한다.
def good_code():
    a, b, v = map(int, input().split())

    day = (v - b) / (a - b)

    print(int(day) if day == int(day) else int(day) + 1)
