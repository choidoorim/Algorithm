"""
- BOJ, 1406
- 에디터
- 커서 기준 왼쪽과 오른쪽 배열을 만들어준다.
"""
from sys import stdin
input = stdin.readline
left_word = list(input().strip())   # 커서 기준 왼쪽 배열
right_word = []     # 커서 기준 오른쪽 배열, 커서의 위치가 문자 제일 뒤부터 시작이므로 빈 배열
t = int(input())

for _ in range(t):
    command = list(map(str, input().split()))
    if command[0] == 'L':
        if left_word:
            right_word.append(left_word.pop())
    elif command[0] == 'D':
        if right_word:
            left_word.append(right_word.pop())
    elif command[0] == 'B':
        if left_word:
            left_word.pop()
    else:
        left_word.append(command[1])
left_word.extend(reversed(right_word))
print("".join(left_word))
