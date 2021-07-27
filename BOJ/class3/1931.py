n = int(input())
array = [] * n
for i in range(n):
    start, end = map(int, input().split())
    array.append((start, end))

array.sort(key=lambda x:(x[1], x[0]))

end_time = 0
count = 0
for arr in array:
    if arr[0] >= end_time:  # 시작 시간과 end time 이 같거나 같을 경우
        end_time = arr[1]
        count += 1
print(count)
