n = int(input())
num_list = list(map(int, input().split()))
cnt = 0


def decimal(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for j in num_list:
    if decimal(j):
        cnt += 1
print(cnt)
