import sys


def my_code():  # 메모리 초과
    n = int(sys.stdin.readline())
    array = []
    for i in range(n):
        array.append(int(sys.stdin.readline()))

    array.sort()

    for i in array:
        print(i)


def sort_num(array):
    for i in range(len(array)):
        min_value = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_value]:
                min_value = j
        array[i], array[min_value] = array[min_value], array[i]
        print(array[i])
# sort_num(array)


def good_code():
    n = int(sys.stdin.readline())
    check_list = [0] * 10001

    for i in range(n):
        num = int(sys.stdin.readline())
        check_list[num] += 1

    for i in range(10001):
        if check_list[i] == 0:
            continue
        for j in range(check_list[i]):
            print(i)


my_code()
