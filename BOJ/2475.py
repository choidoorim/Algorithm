array = list(map(int, input().split()))
check_sum = 0

for i in array:
    check_sum += i * i

print(check_sum % 10)
