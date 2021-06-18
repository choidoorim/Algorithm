def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start   # 가장 왼쪽 값을 피봇 값으로 설정
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[pivot] >= array[left]:  # pivot 값보다 큰 값을 찾기 위한 과정, left 값이 end 값보다 커질 경우 중지
            left += 1   # pivot 값 보다 클 경우 while 문 탈출
        while right > start and array[pivot] <= array[right]:   # pivot 값보다 작은 값을 찾기 위한 과정, right 값이 start 값보다 작을 경우 중지
            right -= 1  # pivot 값 보다 작을 경우 while 문 탈출
        if left > right:    # 엇갈린 경우 오른쪽의 값과 피봇 값을 변경해준다.
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)     # pivot 기준으로 왼쪽
    quick_sort(array, left, end)    # pivot 기준으로 오른쪽
    print(array)


quick_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(quick_array, 0, len(quick_array) - 1)