"""
- Programmers - 다트게임
- CDR
- stack 을 활용.
1. 숫자일 경우 stack 에 넣는다.
2. 보너스 일 경우 배열 내에 숫자에서 마지막 값에 대한 제곱을 수행한다.
3. 옵션 일 경우 '#' 은 -1 을 시켜주고, '*' 일 경우에는 전 값을 2배 시켜주거나
전 값이 없을 경우 현재 값을 2배 시켜준다.
"""


def solution(dartResult):
    array = []
    bonus = {"S": 1, "D": 2, "T": 3}
    dartResult = dartResult.replace('10', 't')    # 10은 '1','0' 2 문자이므로 변환한다.
    for dart in dartResult:
        if dart.isdigit() or dart == 't':
            array.append(10 if dart == 't' else int(dart))
        elif dart in bonus:
            num = array.pop()
            array.append(num ** bonus[dart])
        elif dart == '#':
            num = array.pop()
            array.append(num * -1)
        elif dart == '*':
            num = array.pop()
            if len(array):
                array[-1] *= 2  # 바로 전 점수를 2배로 만듬
            array.append(num * 2)   # '*' 옵션이 처음일 경우
    return sum(array)


print(solution("1D2S#10S"))
