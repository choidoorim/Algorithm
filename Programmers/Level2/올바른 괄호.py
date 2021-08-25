"""
- Programmers - 올바른 괄호
- CDR
"""


def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                del stack[-1]
    if stack:
        return False
    else:
        return True


print(solution("(()("))
