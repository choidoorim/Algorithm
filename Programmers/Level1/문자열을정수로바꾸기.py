def solution(s):
    if s.isdigit():
        return int(s)
    sign = s[0]
    if sign == '-':
        return -1 * int(s[1:])
    else:
        return int(s[1:])


print(solution("+1234"))
