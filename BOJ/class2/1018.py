"""
- BOJ 1018
- CDR
"""
n, m = map(int, input().split())

array = []
result = []

for _ in range(n):
    array.append(input())

for i in range(n - 7):
    for j in range(m - 7):  # 시작점
        w_start = 0   # W 시작일 때의 결과 값
        b_start = 0   # B 시작일 때의 결과 값
        status = array[i][j]
        for k in range(i, i + 8):   # 전체 체스판을 B 와 W 로 번갈아가면서 체크
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:    # 짝, 홀 번째를 나누기 위한 조건
                    if array[k][l] != 'W':  # W 시작인데 0, 2, 4, 6번째 수가 W가 아닌 경우 - w_start 값을 1 증가 시킨다
                        w_start += 1
                    if array[k][l] != 'B':  # B 시작인데 0, 2, 4, 6번째 수가 B가 아닌 경우 - b_start 값을 1 증가 시킨다
                        b_start += 1
                elif (k + l) % 2 == 1:
                    if array[k][l] != 'B':  # W 시작인데 1, 3, 5, 7번째 수가 B가 아닌 경우 - w_start 값을 1 증가 시킨다
                        w_start += 1
                    if array[k][l] != 'W':  # B 시작인데 1, 3, 5, 7번째 수가 W가 아닌 경우 - b_start 값을 1 증가 시킨다
                        b_start += 1
        result.append(w_start)
        result.append(b_start)

print(min(result))
