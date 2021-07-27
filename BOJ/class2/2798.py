# 완전 탐색 문제 - 모든 경우를 다 찾아 고려해야 하는 완전탐색 문제다.
n, m = map(int, input().split())
card = list(map(int, input().split()))
sum_card = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] > m:     # m 값을 넘어갈 경우 무시하고 넘어간다.
                continue
            else:
                sum_card = max(sum_card, card[i] + card[j] + card[k])   # 두 값중 큰 값을 저장한다.

print(sum_card)
# 세 수를 더한 값 중 m 값을 넘지 않는 수 중에서 가장 큰 값을 저장한다