"""
- 백준
- 문제 풀이
문자를 유니코드 값으로 돌려주는 ord 함수를 사용
"""
word = str(input())
alpha = [-1] * 26
for i in range(len(word)):
    if alpha[ord(word[i])-97] == -1:
        alpha[ord(word[i])-97] = i

for ap in alpha:
    print(ap, end=' ')
