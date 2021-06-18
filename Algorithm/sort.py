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


def insertion_sort():   # 기준이 되는 수와 바로 전 수를 비교한다.
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:  # 기존에 정렬을 하면서 진행하기 때문에 마지막과 마지막 전 값 중에서 마지막 값이 크다면 for문을 종료한다.
                break
    print(array)


# insertion_sort()


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[pivot] >= array[left]:  # pivot 값보다 큰 값을 찾기 위한 과정, left 값이 end 값보다 커질 경우 중지
            left += 1
            print(left)
        while right > start and array[pivot] <= array[right]:   # pivot 값보다 작은 값을 찾기 위한 과정, right 값이 start 값보다 작을 경우 중지
            right -= 1
            print(right)
        if left > right:    # 엇갈린 경우 오른쪽의 값과 피봇 값을 변경해준다.
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)     # pivot 기준으로 왼쪽
    quick_sort(array, left, end)    # pivot 기준으로 오른쪽
    print(array)


quick_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(quick_array, 0, len(quick_array) - 1)
