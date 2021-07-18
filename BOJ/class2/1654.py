"""
- BOJ 1654
- CDR
- 이분탐색을 활용하여 풀이
"""
import sys
k, n = map(int, sys.stdin.readline().split())
array = list()
for _ in range(k):
    array.append(int(sys.stdin.readline()))


start = 1
end = max(array)

while start <= end:
    mid = (start + end) // 2

    count = 0
    for arr in array:   # 랜선마다 최대 길이 계산
        count += arr // mid

    if count >= n:  # 원하는 랜선 길이보다 많을 경우, 더 큰 수로 나눠 개수를 줄인다.
        start = mid + 1
    elif count < n:     # 원하는 랜선 길이보다 적을 경우, 더 작은 수로 나눠 개수를 늘린다.
        end = mid - 1

print(end)
