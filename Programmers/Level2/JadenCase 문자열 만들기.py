# capitalize(), title(), capwords() : 문자열의 첫 글자를 대문자로 표시


def solution(s):
    array = s.split(" ")
    for i in range(len(array)):
        array[i] = array[i].capitalize()
    return " ".join(array)


print(solution("3people unFollowed me"))
