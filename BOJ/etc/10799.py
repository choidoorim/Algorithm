"""
- 백준: 10799
- stack 사용
"""
from sys import stdin
input = stdin.readline
s = list(input().rstrip())
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()
            if s[i - 1] == '(':     # 레이저 일 경우
                cnt += len(stack)
            else:
                cnt += 1
print(cnt)

