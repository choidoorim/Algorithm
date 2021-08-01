"""
- BOJ 1789
- CDR
- 1 부터 +1 증가시키면서 각 값을 더한 뒤, 입력 받은 값(s)보다 같거나 커질 경우 출력
"""
s = int(input())
cnt = 1
result = 0
while True:
    result += cnt
    if result >= s:
        print(cnt - 1)
        break
    elif result == s:
        print(cnt)
        break
    cnt += 1
