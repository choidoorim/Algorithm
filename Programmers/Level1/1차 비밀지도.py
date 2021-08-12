"""
- Programmers - 비밀지도
- CDR
"""
from collections import deque


def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    answer = []
    for i in range(n):  # 배열 생성
        array1 = deque(format(arr1[i], 'b'))
        array2 = deque(format(arr2[i], 'b'))
        while len(array1) < n:
            array1.appendleft('0')
        while len(array2) < n:
            array2.appendleft('0')
        map1.append(list(array1))
        map2.append(list(array2))

    for j in range(n):
        result = ""
        for k in range(n):
            if int(map1[j][k]) + int(map2[j][k]) == 0:
                result += " "
            else:
                result += "#"
        answer.append(result)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
