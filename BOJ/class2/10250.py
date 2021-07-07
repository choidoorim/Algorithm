t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())     # 호텔 층 수, 방 수, 몇 번째 손님
    array = [[0]*w for i in range(h)]
    count = 0
    for i in range(w):
        for j in range(h):
            array[j][i] += 1
            count += 1
            if count == n:
                if i + 1 < 10:
                    digit = '0' + str(i + 1)
                else:
                    digit = str(i + 1)
                result = str(j+1) + digit    # 어떻게 십의 자리로 출력할까
                print(result)
                break
