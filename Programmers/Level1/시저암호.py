"""
- Programmers - 시저암호
- CDR
"""


def solution(s, n):
    answer = ''
    for c in s:
        if c == " ":    # 공백
            answer += " "
        elif c.isupper():   # 대문자
            c_num = (ord(c) - ord('A') + n) % 26
            answer += chr(c_num + ord('A'))
        else:   # 소문자
            c_num = (ord(c) - ord('a') + n) % 26
            answer += chr(c_num + ord('a'))
    return answer


print(solution("a B z", 4))
