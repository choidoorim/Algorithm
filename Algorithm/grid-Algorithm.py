import time


def ex():
    array = [3, 4, 2, 4, 7]
    sum = 0
    for x in array:
        sum += x
    print(sum)


# 거스름돈 개수 계산
def change_money(money):
    count = 0
    coin_type = [500, 100, 50, 10]  # 화폐의 종류
    for coin in coin_type:
        count += money // coin  # '//' 연산자는 몫을 표현할 때 사용한다.
        money %= coin
    print(count)


def big_num_fst():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))  # list를 통해 배열로 저장
    start_time = time.time()
    data.sort()  # list 작은 수부터 큰 수 순서로 정렬하기
    fst_num = data[n-1]
    sec_num = data[n-2]
    sum = 0
    while True:
        for x in range(k):  # 0 ~ k-1까지
            if m == 0:
                break
            sum += fst_num
            m -= 1
        sum += sec_num
        m -= 1
        if m == 0:
            break
    end_time = time.time()
    print("time : ", end_time - start_time)
    print(sum)


def big_num_sec():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    start_time = time.time()
    data.sort()
    fst_num = data[n-1]
    sec_num = data[n-2]

    sum = 0
    count = int(m//(k+1)) * k
    count += m % (k+1)

    sum += fst_num * count
    sum += sec_num * (m - count)
    end_time = time.time()
    print("time : ", end_time - start_time)
    print(sum)

big_num_fst()

# start_time = time.time()
# end_time = time.time()
# print("time : ", end_time - start_time)

