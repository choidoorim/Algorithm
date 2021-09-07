n = int(input())
money = list(map(int, input().split()))
m = int(input())
money.sort()
start = 0
end = money[-1]
while start <= end:
    mid = (start + end) // 2
    sum_money = 0
    for i in money:
        if i >= mid:
            sum_money += mid
        else:
            sum_money += i
    if sum_money <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
