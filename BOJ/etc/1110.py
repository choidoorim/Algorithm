n = input()
num = n
cnt = 0
while True:
    if len(num) == 1:
        num = '0' + num
    sum_num = str(int(num[0]) + int(num[1]))
    num = num[-1] + sum_num[-1]
    cnt += 1
    if int(num) == int(n):  # 숫자가 동일하다면 종료
        break
print(cnt)
