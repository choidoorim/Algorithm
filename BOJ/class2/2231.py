# 브루트포스 알고리즘: 모든 수를 다 검사한다.
n = int(input())
result = 0

for i in range(1, n + 1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s == n:
        result = i
        break

print(result)
