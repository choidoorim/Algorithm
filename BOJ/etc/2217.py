"""
- BOJ 2417
- CDR
- 가장 작은 무게를 들 수 있는 로프가 들 수 있는 질량 * 병렬 연결 로프 갯수 = 최종 무게
"""
N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)
for i in range(N):
    array[i] = array[i] * (i + 1)
print(max(array))
