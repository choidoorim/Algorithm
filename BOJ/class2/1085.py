def my_code():
    x, y, w, h = map(int, input().split())
    length = [0] * 4  # 동 서 남 북

    length[0] = h - y  # 동
    length[1] = y  # 서
    length[2] = x  # 남
    length[3] = w - x  # 북

    print(min(length))


def good_code():
    x, y, w, h = map(int, input().split())
    print(min(h-y, y, x, w-x))


good_code()
