n, m = map(int, input().split())
rice = list(map(int, input().split()))

start = 0
end = max(rice)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in rice:  # 떡을 잘랐을 때의 떡의 양 계산
        if i > mid:
            total += i - mid
    if total < m:   # 더 많이 잘릴 경우
        end = mid - 1
    else:   # 떡이 덜 잘릴 경우는 없다.
        result = mid
        start = mid + 1

print(result)
