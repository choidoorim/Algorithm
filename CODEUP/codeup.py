# <코드잇>
# 정수: int/실수: float
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift) -> 비트단위 연산자.
# float 와 double의 차이점은 double이 수의 오차범위가 더 작다라는 것이다.
# a ** b -> a^b 이다.
# 코드를 통해 예외처리를 작성해주는 것만으로 컴파일 시간과 메모리를 효율적으로 사용할 수 있다.
# EX) codeup_98() -> 예외 처리를 하지 않았다가 코드업에서 시간 초과로 코드 제출이 되지 않았다.
# unicode로 입력 받은 문자를 변환.
# UniCode: 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하는 것.
def codeup_06():
    print("\"!@#$%^&*()\'")


def codeup_19():
    y, m, d = input().split('.')
    print(d, m, y, sep='-')


def codeup_20():
    fst, sec = input().split('-')
    print(fst, sec, sep='')


def codeup_21():
    fst = input()
    a = len(fst)
    for i in range(a):
        print(fst[i])


def codeup_22():
    s = input()
    print(s[0:2])
    print(s[2:4])
    print(s[4:6])


def codeup_23():
    a, b, c = input().split(':')
    print(b)


def codeup_24():
    word1, word2 = input().split()
    s = word1 + word2
    print(s)


def codeup_25():
    word1, word2 = input().split()
    s = int(word1) + int(word2)
    print(s)


def codeup_26():
    word1 = input()
    word2 = input()
    s = float(word1) + float(word2)
    print(s)


def codeup_27():
    word1 = input()
    a = int(word1)
    print('%x' % a)


def codeup_28():
    word1 = input()
    a = int(word1)
    print('%X' % a)  # %x -> 소문자 출력, %X -> 대문자 출력


def codeup_29():
    word1 = input()
    a = int(word1, 16)  # 입력된 a를 16진수로 변환
    print('%o' % a)


def codeup_30():
    word1 = ord(input())
    print(word1)


def codeup_31():
    word1 = int(input())
    print(chr(word1))


def codeup_32():
    word1 = int(input())
    print(-word1)


def codeup_33():
    word1 = ord(input())  # unicode로 입력 받은 문자를 변환.
    word2 = word1 + 1
    print(chr(word2))


def codeup_34():
    a, b = input().split()
    c = int(a) - int(b)
    print(c)


def codeup_35():
    a, b = input().split()
    c = float(a) * float(b)
    print(c)


def codeup_36():
    word1, n = input().split()
    print(word1 * int(n))


def codeup_37():
    n = input()
    word1 = input()
    print(int(n) * word1)


def codeup_38():
    w1, w2 = input().split()
    print(int(w1) ** int(w2))


def codeup_39():
    w1, w2 = input().split()
    print(float(w1) ** float(w2))


def codeup_40():
    w1, w2 = input().split()
    print(int(w1) // int(w2))  # '//'연산자는 몫을 계산해준다.


def codeup_41():
    w1, w2 = input().split()
    print(int(w1) % int(w2))


def codeup_42():  # 정확도 측정은 round를 통해 계산해야한다.
    w1 = input()
    print(round(float(w1), 2))


def codeup_43():
    w1, w2 = input().split()
    result = float(w1) / float(w2)  # 실수가 컴퓨터에 저장되는 과정에서 잘림 오차가 자주 발생한다.
    print('%.3f' % result)


def codeup_44():
    w1, w2 = input().split()
    print(int(w1) + int(w2))
    print(int(w1) - int(w2))
    print(int(w1) * int(w2))
    print(int(w1) // int(w2))
    print(int(w1) % int(w2))
    result = float(w1) / float(w2)
    print(round(float(result), 2))


def codeup_45():
    w1, w2, w3 = input().split()
    sum = int(w1) + int(w2) + int(w3)
    rv = sum / 3
    print(sum, round(rv, 2))


def codeup_46():
    n = input()
    shift = int(n) << 1  # << 왼쪽 쉬프트. >> 오른쪽 쉬프트.
    print(shift)


def codeup_47():
    n1, n2 = input().split()
    print(int(n1) << int(n2))


def codeup_48():
    n1, n2 = input().split()
    print(int(n1) < int(n2))  # 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다)


def codeup_49():
    n1, n2 = input().split()
    print(int(n1) == int(n2))


def codeup_50():
    n1, n2 = input().split()
    print(int(n1) <= int(n2))


def codeup_51():
    n1, n2 = input().split()
    print(int(n1) != int(n2))


def codeup_52():
    n = int(input())
    print(bool(n))


def codeup_53():
    n = bool(int(input()))
    print(not n)


def codeup_54():
    n1, n2 = input().split()
    print(bool(int(n1)) and bool(int(n2)))


def codeup_55():
    n1, n2 = input().split()
    print(bool(int(n1)) or bool(int(n2)))


def codeup_56():
    n1, n2 = input().split()
    print((bool(int(n1)) and (not bool(int(n2)))) or ((not bool(int(n1))) and bool(int(n2))))


def codeup_57():
    n1, n2 = input().split()
    print((bool(int(n1)) or (not bool(int(n2)))) and ((not bool(int(n1))) or bool(int(n2))))


def codeup_58():
    n1, n2 = input().split()
    print(not (bool(int(n1)) or bool(int(n2))) and not (bool(int(n1)) or bool(int(n2))))


def codeup_59():
    n1 = int(input().split())
    print(~n1)


def codeup_60():
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    print(n1 & n2)


def codeup_61():
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    print(n1 | n2)


def codeup_62():
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    print(n1 ^ n2)


def codeup_63():
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    if (n1 > n2):
        print(n1)
    else:
        print(n2)


def codeup_63_1():
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    result = (n1 if (n1 > n2) else n2)
    print(result)


def codeup_64():
    n1, n2, n3 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    print((n2 if (n1 > n2) else n1) if ((n2 if (n1 > n2) else n1)) < n3 else n3)


def codeup_64_1():
    n1, n2, n3 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if (n1 > n2):
        small = n2
        if (small < n3):
            small = small
        else:
            small = n3
    elif (n1 < n2):
        small = n1
        if (small < n3):
            small = small
        else:
            big = n3
    print(int(small))


def codeup_65():
    n1, n2, n3 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if (n1 % 2 == 0):
        print(int(n1))
    if (n2 % 2 == 0):
        print(int(n2))
    if (n3 % 2 == 0):
        print(int(n3))


def num(number):
    if (number % 2 == 0):
        print("even")
    else:
        print("odd")


def codeup_66():
    n1, n2, n3 = input().split()
    num(int(n1))
    num(int(n2))
    num(int(n3))


def Judge(num):
    if (num % 2 == 0 and num < 0):
        print("A")
    elif (num % 2 != 0 and num < 0):
        print("B")
    elif (num % 2 == 0 and num > 0):
        print("C")
    else:
        print("D")


def codeup_67():
    n1 = int(input())
    Judge(n1)


def ev(num):
    if (num >= 90):
        print("A")
    elif (90 > num >= 70):
        print("B")
    elif (70 > num >= 40):
        print("C")
    else:
        print("D")


def codeup_68():
    n1 = int(input())
    ev(n1)


def codeup_69():
    n1 = str(input())
    if (n1 == "A"):
        print("best!!!")
    elif (n1 == "B"):
        print("good!!")
    elif (n1 == "C"):
        print("run!")
    elif (n1 == "D"):
        print("slowly~")
    else:
        print("what?")


def season(num):
    if (num == 12):
        num = 1
    else:
        num = int(num)

    result = num / 3
    result = int(result)
    if (result == 0):
        print("winter")
    elif (result == 1):
        print("spring")
    elif (result == 2):
        print("summer")
    elif (result == 3):
        print("fall")
    else:
        print("Not Season")


def codeup_70():
    n1 = int(input())
    season(n1)


def season_2(num):
    if (num == 1 or num == 12 or num == 2):
        print("winter")
    elif (num == 3 or num == 4 or num == 5):
        print("spring")
    elif (num == 6 or num == 7 or num == 8):
        print("summer")
    elif (num == 9 or num == 10 or num == 11):
        print("fall")
    else:
        print("Not Season.")

def codeup_71():
    n1 = 1  # 초기 값
    while n1 != 0:
        n1 = int(input())  # 키보드를 통해 입력하는 숫자는 형변환을 해주지 않으면 str형으로 입력이 된다.
        print(type(n1))
        if (n1 != 0):
            print(n1)


def codeup_72():
    n1 = int(input())
    while n1 != 0:
        print(n1)
        n1 = n1 - 1


def codeup_73():
    n1 = int(input())
    while n1 != 0:
        n1 = n1 - 1
        print(n1)


def codeup_74():  # ord(): 문자를 아스키코드 값으로 변환해주는 함수, chr():아스키코드 값을 문자로 변환해주는 함수
    n1 = ord(input())
    n2 = ord('a')  # 초기 값 a의 아스키코드
    while n2 <= n1:
        print(chr(n2), end=' ')  # print(..., end=' ')로 입력 시 줄을 바꾸지 않고 공백문자를 출력한다.
        n2 += 1


def codeup_75():
    n1 = int(input())
    n2 = 0
    while n2 <= n1:
        print(n2)
        n2 += 1


def codeup_76():  # 반복문 변수의 순서는 i,j,k..알파벳순으로 사용한다.
    n1 = int(input())
    for i in range(n1 + 1):  # range(n) 함수는 0 ~ n-2, n-1 까지의 수열을 의미한다.
        print(i)


def codeup_77():
    n1 = int(input())
    sum = 0
    for i in range(n1 + 1):
        if (i % 2 == 0):
            sum += i
    print(sum)


def codeup_78():
    n1 = ''
    while n1 != 'q':
        n1 = input()
        print(n1)


def codeup_78_1():
    n1 = input().split()
    for i in n1:
        print(i)
        if (i == 'q'):
            break


def codeup_79():
    n1 = int(input())
    sum = 0
    i = 0
    while n1 > sum:
        i += 1
        sum = sum + i
    print(i)


def codeup_80():
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    for i in range(1, n1 + 1):  # 1 ~ n1까지
        for j in range(1, n2 + 1):  # 1 ~ n2까지
            print(i, j)


def codeup_81():
    n1 = input()
    n1 = int(n1, 16)  # n1을 16진수로 변환.
    for i in range(1, 16):  # i는 int형이다.
        print('%X*%X=%X' % (n1, i, (n1 * i)))
        # print('%X'%n1,'*%X ='%i,' %X'%(n1*i), sep='') #sep='' : 공백 없이 붙여서 출력해준다.


def codeup_82():  # 비효율적인 코드
    n1 = int(input())
    j = 0
    for i in range(1, n1 + 1):
        j += 1  # 1의 자리수만 계산하기 위한 변수
        if (j == 11):
            j = 1
        if (j % 3 == 0):
            print('X', end=' ')
        else:
            print(i, end=' ')


def codeup_82_1():
    n1 = int(input())
    for i in range(1, n1 + 1):
        if (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
            print('X', end=' ')
        else:
            print(i, end=' ')


def codeup_83():  # 반복문을 통해 데이터를 변수에 넣고 한번에 출력하는 것이 매번 출력하는 것보다 빠르다.
    n1, n2, n3 = map(int, input().split())
    ic = 0
    for i in range(n1):
        for j in range(n2):
            for k in range(n3):
                print('{} {} {}'.format(i, j, k))  # print(i,j,k)보다 format을 통해 출력하는 것이 더 빠르다.
                ic += 1
    print(ic)


def codeup_84():
    h, b, c, s = map(int, input().split())
    result = round(float(h * b * c * s / 8 / 1024 / 1024), 1)
    print('{} MB'.format(result))


def codeup_85():
    w, h, b = map(int, input().split())
    result = w * h * b / 8 / 1024 / 1024
    print('%.2f MB' % result)


def codeup_86():
    n1 = int(input())
    ic = 0
    sum = 0
    while True:
        ic += 1
        sum += ic
        if (sum >= n1):
            print(sum)
            break


def codeup_87():
    n1 = int(input())
    for i in range(1, n1 + 1):
        if (i % 3 == 0):
            continue  # 조건문이나 반복문에 continue가 실행되면 다음 반복단계로 넘어간다.
            print(type(n1))  # 실행되지 않고 넘어간다.
        else:
            print(i, end=' ')


def codeup_88():  # 등차수열
    a, d, n = map(int, input().split())
    result = a + (n - 1) * d
    print(result)


def codeup_89():  # 등비수열
    a, r, n = map(int, input().split())
    result = a * (r ** (n - 1))
    print(result)


def codeup_90():  # 수열
    a, m, d, n = map(int, input().split())
    for i in range(1, n):  # a 값에서부터 반복문이 1번 실행된것과 같다.
        seq = a * m + d
        a = seq  # 결과 값을 저장.
    print(a)  # 1 -1 1 1을 넣었을 때는 1번째 순서이므로 반복문이 돌지 않고 실행되는 것과 같으므로 seq가 아닌 a를 출력해야한다.


def codeup_91():  # 나머지 값을 통해서 최소공배수를 계산할 수 있다.
    a, b, c = map(int, input().split())
    ic = 1
    while (ic % a != 0 or ic % b != 0 or ic % c != 0):
        ic += 1
    print(ic)


def codeup_91_1():
    a, b, c = map(int, input().split())
    ic = 1
    while True:
        ic += 1
        if (ic % a == 0 and ic % b == 0 and ic % c == 0):
            break
    print(ic)


def codeup_92():
    n = int(input())
    a = input().split()
    for i in range(0, n):  # n번 a 번호를 입력하여 저장
        a[i] = int(a[i])

    d = []
    for i in range(24):  # count된 수를 담을 list
        d.append(0)

    for i in range(n):  # a list에 값이 있을 때마다 d list의 해당 숫자 count
        d[a[i]] += 1

    for i in range(1, 24):
        print(d[i], end=' ')


def codeup_93():
    n = int(input())
    a = input().split()
    for i in range(0, n):  # n번 a 번호를 입력하여 저장
        a[i] = int(a[i])

    for i in range(n - 1, -1, -1):
        print(a[i], end=' ')


def codeup_94():
    n = int(input())
    a = input().split()
    for i in range(0, n):  # n번 a 번호를 입력하여 저장
        a[i] = int(a[i])
    sma = a[0]  # 가장 작은 값을 지정

    for i in range(0, n):  # 비교 로직
        if (sma > a[i]):
            sma = a[i]
        else:
            sma = sma
    print(sma)


def codeup_95():
    d = []  # d= list() 2가지 방법으로 빈 리스트를 생성할 수 있다.
    for i in range(0, 20):  # 0 ~ 19까지인 리스트 생성, 빈 리스트는 항상 0부터 시작.
        d.append([])  # 기존 리스트에서 새로운 리스트 만들기. = List Comprehensions
        # [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        for j in range(0, 20):
            d[i].append(0)  # 새로 생긴 리스트마다 0 값을 20번 채워준다.

    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        d[a][b] = 1

    for i in range(1, 20):  # 1~20 리스트중에 0~19까지의 리스트만 사용
        for j in range(1, 20):
            print(d[i][j], end=' ')
        print()


def codeup_96():
    d = []
    for i in range(20):  # 20개의 바둑판을 만들지만 (1~19) - (1~19)의 바둑판만 사용한다.
        d.append([])
        for j in range(20):
            d[i].append(0)

    x = list()
    for i in range(19):  # range를 (1,20)으로 했을 때는 list을 벗어나는 오류가 발생한다. 왜냐하면 x는 새로운 리스트로 0부터 시작이기 때문이다.
        x = input().split()  # 19개의 값을 입력(0 ~ 19)
        for j in range(19):
            d[i + 1][j + 1] = int(x[j])

    n = int(input())  # 몇번 행과 열을 바꿀지 입력
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(1, 20):
            if d[a][j] == 0:
                d[a][j] = 1
            else:
                d[a][j] = 0

            if d[j][b] == 0:
                d[j][b] = 1
            else:
                d[j][b] = 0

    for i in range(1, 20):
        for j in range(1, 20):
            print(d[i][j], end=' ')
        print()


def codeup_97():
    w, h = map(int, input().split())
    n = int(input())  # 몇개의 막대를 추가할지 입력
    ls = list()
    for k in range(w + 1):  # 입력한 배열보다 1개의 행과 열을 추가한다.
        ls.append([])
        for l in range(h + 1):
            ls[k].append(0)

    for k in range(n):  # 입력받은 막대의 개수
        i, d, x, y = map(int, input().split())
        for l in range(i):  # 막대의 길이
            if (d == 0):  # 0일 경우 입력받은 가로 값은 유지하고 세로 값들을 하나씩 추가한다.
                ls[x][y + l] = 1
            else:  # 1일 경우 입력받은 세로 값은 유지하고 가로 값들을 하나씩 추가한다.
                ls[x + l][y] = 1

    for k in range(1, w + 1):
        for l in range(1, h + 1):
            print(ls[k][l], end=' ')
        print()


def codeup_98():
    # 10*10 맵 입력 리스트에서의 2, 2는 3번째 행과 열이지만
    # 문제에서의 2, 2는 2번째 행과 열이기 때문에 11*11을 생성 후 값을 1,1부터 넣어줘야 한다.
    d = []
    for i in range(11):  # 11 * 11 리스트 생성
        d.append([])
        for j in range(11):
            d[i].append(0)
    for i in range(10):
        x = input().split()
        for j in range(10):
            d[i + 1][j + 1] = int(x[j])
    a, b, status = 2, 2, 0
    while True:
        d[a][b] = 9
        if (status == 2):
            break

        # 예외 처리문을 통해 메모리와 컴파일 시간을 단축 시킬 수 있다. (중요!!!!!)
        if (d[a][b + 1] == 1 and d[a + 1][b] == 1) or (a == 9 and b == 9):
            break

        if (d[a][b + 1] != 1):
            b += 1
            status = d[a][b]
        elif (d[a + 1][b] != 1):
            a += 1
            status = d[a][b]

    for i in range(1, 11):  # 11 * 11 리스트 생성
        for j in range(1, 11):
            print(d[i][j], end=' ')
        print()


def lrud():
    n = int(input())
    x, y = 1, 1
    plans = input().split()
    for plan in plans:
        print(x, y)
        if plan == 'L':
            nx = x
            ny = y - 1
        elif plan == 'R':
            nx = x
            ny = y + 1
        elif plan == 'U':
            nx = x - 1
            ny = y
        elif plan == 'D':
            nx = x + 1
            ny = y
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        x, y = nx, ny
    print(x, y)


def time():
    n = int(input())
    count = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)


def knight():
    location = input()
    row = int(location[1])
    column = ord(location[0]) - ord('a') + 1
    count = 0
    move_type = [(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
    for move in move_type:
        next_row = row + move[0]
        next_column = column + move[1]
        if 0 < next_row <= 8 and 0 < next_column <= 8:
            count += 1
    print(count)



def change_money(money):
    coin_type = [500, 100, 50, 10]
    count = 0
    for coin in coin_type:  # coin에 500, 100, 50 ,10이 들어감
        print(coin)
        count += money//coin
        money %= coin
    print(count)


def big_num():
    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    fst_num = data[n-1]
    sec_num = data[n-2]

    count = (m // (k+1)) * k    # 수열이 반복되는 수 * 큰 수를 곱할 수 있는 최대 수
    count += m % (k+1)

    result = 0
    result += fst_num * count
    result += sec_num * (m-count)
    print(result)