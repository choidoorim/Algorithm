# dictionary 를 사용하여 숫자영어와 그에 해당하는 숫자를 정의
def solution(s):
    answer = ''
    eng = ''
    number = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }
    for i in s:
        if i.isdigit():
            answer += i
        else:
            eng += i
            if eng in number:
                answer += str(number[eng])
                eng = ''
    return int(answer)


print(solution("2three45sixseven"))
