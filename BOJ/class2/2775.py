def my_code():  # 파이썬의 장점을 살리지 못한 지저분한 코드
    t = int(input())

    for i in range(t):
        k = int(input())
        n = int(input())
        array = [1] * n
        sum_num = 0
        for _ in range(k + 1):  # 층
            result = [0] * n
            for m in range(0, n):  # 호
                for o in range(m + 1):
                    sum_num += array[o]
                result[m] += sum_num
                sum_num = 0
            for p in range(len(array)):
                array[p] = result[p]
        print(array[n - 1])


def good_code():
    t = int(input())

    for i in range(t):
        k = int(input())
        n = int(input())

        d = [j for j in range(1, n + 1)]

        for l in range(k):
            for m in range(1, n): # d[0]은 항상 1로 고정이기 때문
                d[m] += d[m - 1]
        print(d[n - 1])


good_code()
