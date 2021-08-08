"""
- BOJ 10816
- CDR
- 해시 알고리즘을 사용: 해시 알고리즘 - 키와 값 쌍으로 이루어진 데이터 구조
  python -> dict(), {}
  시간이 빠르다는 장점을 가지고 있다.
- https://davinci-ai.tistory.com/19 - 해시 알고리즘 참고 URL
"""
import sys


def binary_search(num, arr, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == num:
        return arr.count(num)   # 숫자를 찾았을 때 배열 내 몇개가 있는지 반환 한다.
    elif arr[mid] < num:
        return binary_search(num, arr, mid + 1, end)
    else:
        return binary_search(num, arr, start, mid - 1)


def my_code():  # 시간초과 발생
    n = int(sys.stdin.readline())
    n_array = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    m_array = list(map(int, sys.stdin.readline().split()))

    for i in range(m):
        print(binary_search(m_array[i], n_array, 0, n - 1), end=' ')


def good_code():
    n = int(sys.stdin.readline())
    n_array = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    m_array = list(map(int, sys.stdin.readline().split()))

    dictionary = dict()  # 키 값과 값의 쌍으로 이루어져있다.

    for i in n_array:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    for target in m_array:
        if target in dictionary:
            print(dictionary[target], end=' ')
        else:
            print(0, end=' ')


good_code()