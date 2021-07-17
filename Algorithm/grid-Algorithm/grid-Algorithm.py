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

# change_money(1260)

def big_num_fst():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))  # list를 통해 배열로 저장
    data.sort()  # list 작은 수부터 큰 수 순서로 정렬하기
    fst_num = data[n - 1]
    sec_num = data[n - 2]
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
    print(sum)



def big_num():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort()
    fst_num = data[n - 1]
    sec_num = data[n - 2]

    sum = 0
    count = int(m // (k + 1)) * k
    count += m % (k + 1)

    sum += fst_num * count
    sum += sec_num * (m - count)
    print(sum)

# big_num()

# 제일 작은 수의 카드 값중 제일 큰 것 고르기
def card_select_fst():
    result = 0
    n, m = map(int, input().split())
    for x in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)  # min 함수는 list중에 제일 작은 수를 찾아준다.
        result = max(result, min_value)
    print(result)

# card_select_fst()

def card_select_sec():
    n, m = map(int, input().split())  # n -  행, m - 열
    result = 0
    for x in range(n):
        data = list(map(int, input().split()))
        min_value = 10001
        for y in data:  # 행 중에서 가장 작은 값을 추출
            min_value = min(y, min_value)
        print(min_value)
        result = max(result, min_value)
    print(result)


# 한 번 나누기를 시작하면 계속 나누기를 한다.
def fromOne():
    n, k = map(int, input().split())
    count = 0
    while True:
        if n % k != 0:
            n -= 1
            count += 1
        n //= k
        count += 1
        if n < k:
            break
    print(count)

fromOne()

# 곱하기 혹은 더하기 - 1까지는 더하기가 더 효율적이고 2부터는 곱하기가 더 효율적이다.
def ex():
    data = input()
    result = int(data[0])  # 첫번째 수를 저장
    count = 0

    for x in range(1, len(data)):
        num = int(data[x])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)


# 상하좌우
def lrud():
    n = int(input())
    plans = input().split()
    x, y, nx, ny = 1, 1, 1, 1
    for plan in plans:
        print(x, y)
        if plan == 'L':
            ny = y - 1
        elif plan == 'R':
            ny = y + 1
        elif plan == 'U':
            nx = x - 1
        elif plan == 'D':
            nx = x + 1
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # nx, ny를 통해 위에 조건을 충족하지 못할 경우 x, y를 업데이트 하는 과정을 무시
        x, y = nx, ny
    print(x, y)


def lrud_fst():
    n = int(input())
    x, y = 1, 1
    plans = input().split()
    move_type = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for plan in plans:
        for i in range(len(move_type)):
            if plan == move_type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or nx > n:
            continue
        x, y = nx, ny
    print(x, y)


# 시각
def time():
    h = int(input())
    count = 0
    for i in range(h + 1):  # range는 n-1 까지 계산하므로 0 ~ h까지의 시간을 반복문으로 사용하기 위해서 h + 1
        for j in range(60):  # 0 ~ 59분까지
            for k in range(60):  # 0 ~ 59초까지
                if '3' in str(i) + str(j) + str(k):  # int 값을 합칠 때는 str을 더하는 것도 방법중 하나이다.
                    count += 1
    print(count)


# 왕실의 나이트
def knight():
    input_data = input()
    row = int(input_data[1])
    column = ord(input_data[0]) - ord('a') + 1  # 열을 숫자로 변환(a ~ h)
    count = 0
    move_type = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]  # 체스말이 움직일 수 있는 유형
    for move in move_type:  # 유형들이 움직일 수 있는 범위안에 들어가는지 체크 
        # row += move[0] 기존의 값이 변경되어 측정을 할 수가 없음.
        # column += move[1] 따라서 새로운 변수에 값을 저장하는 방식으로 진행해야함.
        next_row = row + move[0]
        next_column = column + move[1]
        print(move, next_row, next_column)
        if 0 < next_row <= 8 and 0 < next_column <= 8:  # 움직였을 때 해당 말들이 범위 안에 들어오는지에 대한 여부
            count += 1
    print(count)


# 문자열 재정렬
def sort():
    words = input()
    result = []
    value = 0

    for word in words:
        if word.isalpha():  # 문자가 알파벳인지 확인
            result += word
        else:
            value += int(word)  # 숫자는 int 형으로 변환 후 더함.
    result.sort()  # 오름차순으로 정렬
    if value != 0:  # 숫자가 있을 경우에만 합침
        result.append(str(value))
    print(''.join(result))  # 리스트를 문자열로 변경


# 게임 개발
def game():
    n, m = map(int, input().split())
    move = [m * [0] for _ in range(n)]

    x, y, location = map(int, input().split())
    move[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 1
    turn_count = 0

    maps = []
    for i in range(n):
        maps.append(list(map(int, input().split())))

    while True:
        location -= 1
        if location == -1:
            location = 3
        nx = x + dx[location]
        ny = y + dy[location]
        if move[nx][ny] == 0 and maps[nx][ny] == 0:
            move[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_count = 0
        else:
            turn_count += 1
        if turn_count == 4:
            nx = x - dx[location]
            ny = y - dy[location]
            if move[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_count = 0
    print(count)

# game()

# start_time = time.time()
# end_time = time.time()
# print("time : ", end_time - start_time)
