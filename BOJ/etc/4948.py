def find_num(num):
    if num == 1:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


array = list(range(2, 246912))
save_array = []
for i in array:
    if find_num(i):
        save_array.append(i)


while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for i in save_array:
            if n < i <= n * 2:
                cnt += 1
    print(cnt)
