from sys import stdin
x = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

result = [0] * 100  # 최대 100까지
result[0] = array[0]
result[1] = max(array[0], array[1])

# 전 창고는 털지 못하므로 전 창고까지의 식량 합과 (전전 창고까지의 식량합 + 현재 식량)을 더한 값을 비교 후 결과를 저장
for i in range(2, x):
    result[i] = max(result[i - 1], result[i - 2] + array[i])

print(result[x - 1])
