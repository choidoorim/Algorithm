"""
- BOJ 2579
- CDR
- 다이나믹 프로그래밍
- 어떻게 올라갈지가 아닌 어디서부터 올라온건지를 생각하여 풀이를 해야 합니다
  연속된 3칸을 올라가지 못하기 때문에
  1. 현재 위치 계단 + 한 단계 아래 계단  + 3칸 밑의 dp 값
  2. 현재 위치 계단 + 2칸 밑의 dp 값
  1, 2 번중 큰 값을 dp 에 저장하는 방식으로 풀이를 했습니다
"""
t = int(input())
array = [0]
for _ in range(t):
    array.append(int(input()))

if t == 1:
    print(array[1])
else:
    d = [0] * (t + 1)
    d[1] = array[1]
    d[2] = array[1] + array[2]
    for i in range(3, t + 1):
        d[i] = max(d[i - 3] + array[i] + array[i - 1], d[i - 2] + array[i])
    print(d[t])

