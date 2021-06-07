import time


def ex():
    array = [3, 4, 2, 4, 7]
    sum = 0
    for x in array:
        sum += x
    print(sum)


start_time = time.time()  # 알고리즘 실행 시간 확인
ex()
end_time = time.time()
print("time : ", end_time - start_time)
