# 선택 정렬
def my_select_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    change_value = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                change_value = array[j]
                array[j] = array[i]
                array[i] = change_value
            print(array, change_value)

# my_select_sort()


def select_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(len(array)):
        min_value = i
        for j in range(i + 1, len(array)):  # 가장 작은 값을 찾는다.
            if array[min_value] > array[j]:
                min_value = j
            print(array, min_value)
        array[i], array[min_value] = array[min_value], array[i]     # for문이 끝나면 가장 작은 값과 기준 값을 스와이프 처리
        # print(array, min_value)


# select_sort()


def insertion_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:  # 기존에 정렬을 하면서 진행하기 때문에 마지막과 마지막 전 값 중에서 마지막 값이 크다면 for문을 종료한다.
                break
    print(array)


insertion_sort()
