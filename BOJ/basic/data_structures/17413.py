"""
- BOJ, CDR
- 17413
- '<' 이 나왔을 경우 '>' 이 나올 때까지 단어를 뒤집지 않고,
  일반적으로 거꾸로 단어를 더하다가 ' ' 띄어쓰기가 나왔을 때 결과 값에 합친다.
"""

from sys import stdin
input = stdin.readline
s = list(input().rstrip())
result = ''
word = ''
flag = False
for i in s:
    if not flag:
        if i == '<':
            flag = True
            word = word + i
        elif i == ' ':  # 띄어쓰기가 나왔을 경우 만든 단어를 result 에 합친다.
            word = word + i
            result = result + word
            word = ''
        else:   # 거꾸로 단어를 만든다.
            word = i + word
    elif flag:
        word = word + i
        if i == '>':
            flag = False
            result = result + word
            word = ''
print(result+word)
