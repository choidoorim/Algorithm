minute, second = map(int, input().split())

if second - 45 < 0:
    if minute - 1 < 0:
        minute = 23
    else:
        minute -= 1
    second = 60 + (second - 45)
else:
    second -= 45

print(minute, second)
