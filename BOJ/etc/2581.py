m = int(input())
n = int(input())


def find(num):
    if num == 1:
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True


sum_num = 0
result = []
for i in range(m, n + 1):
    if find(i):
        sum_num += i
        result.append(i)

if not result:
    print(-1)
else:
    print(sum_num)
    print(min(result))
