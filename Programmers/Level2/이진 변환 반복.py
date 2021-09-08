def solution(s):
    cnt = 0
    zero = 0

    while True:
        if s == '1':
            break
        zero += s.count("0")
        s = s.replace("0", "")
        s = format(len(s), 'b')
        cnt += 1

    answer = [cnt, zero]
    return answer


print(solution("110010101001"))
