"""
- BOJ 1541
- CDR
- 화폐가 잔돈보다 클 경우를 계산하기 위한 조건문. (ex.잔돈200 % 화폐500 = 잔돈200 이라는 것을 활용 )
- 잔돈을 화폐로 나눈 나머지의 값이 기존 잔돈과 같을 경우가 아닐 경우만 계산
"""
N = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in money:
    if N != N % i:
        cnt += N // i
        N %= i
print(cnt)
