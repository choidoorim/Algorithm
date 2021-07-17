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
        array[i], array[min_value] = array[min_value], array[i]     # for문이 끝나면 가장 작은 값과 기준 값을 스와이프 처리
    print(array)


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


# quick_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# quick_sort(quick_array, 0, len(quick_array) - 1)

def count_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    count_array = [0] * (max(array) + 1)  # 배열에서 가장 큰 값을 찾은 후, 0~max 값 계수 배열을 만든다.
    for i in array:  # 데이터를 확인하면서 동일한 데이터를 1씩 증가시킨다.
        count_array[i] += 1
    print(count_array)

    for i in range(len(count_array)):
        for j in range(count_array[i]):
            print(i, end=' ')


# count_sort()


def up_down():
    n = int(input())

    array = []
    for i in range(n):
        array.append(int(input()))

    for i in range(len(array)):
        min_value = i
        for j in range(i + 1, len(array)):
            if array[min_value] > array[j]:
                min_value = j
        array[i], array[min_value] = array[min_value], array[i]

    for i in range(len(array) - 1, -1, -1):
        print(array[i], end=' ')


# up_down()


def up_down_library():
    n = int(input())

    array = []
    for i in range(n):
        array.append(int(input()))

    array = sorted(array, reverse=True)

    for i in array:
        print(i, end=' ')


# up_down_library()

def grade():
    n = int(input())


def grade_library():
    n = int(input())

    array = []
    for i in range(n):
        data = input().split()
        array.append((data[0], int(data[1])))   # 튜플(리스트)은 수정, 삽입, 삭제가 되지 않기 때문에 sorted method를 사용해야 한다.

    array = sorted(array, key=lambda a: a[1])   # array라는 배열의 점수([1]) 리스트를 기준으로 정렬함.

    for student in array:
        print(student[0], end=' ')


# grade_library()


def change():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()  # 오름차순으로 정렬
    b.sort(reverse=True)  # 내림차순으로 정렬

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    sum = 0
    for i in range(len(a)):
        sum += a[i]

    print(sum)


# change()


def change_two():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()  # 오름차순으로 정렬
    b.sort(reverse=True)  # 내림차순으로 정렬

    for i in range(k):  # a 배열의 가장 작은 값과, b 배열의 가장 큰 값을 바꿔준다.
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    print(sum(a))


change_two()