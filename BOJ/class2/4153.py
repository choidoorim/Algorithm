while True:
    num = list(map(int, input().split()))
    num.sort()  # 오름차순으로 정렬
    max_num = max(num)  # 가장 큰 값이 빗변
    if sum(num) == 0:
        break

    if max_num**2 == num[0]**2 + num[1]**2:
        print('right')
    else:
        print('wrong')
