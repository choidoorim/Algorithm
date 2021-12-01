"""
- 프로그래머스
- CDR
- x:x*3 : number 인자의 각각의 문자열을 3번 반복한다는 뜻.
num 의 인수 값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻입니다.
- [0, 0, 0, 0] => 0000을 리턴하므로 0일 때의 제어처리를 해줘야 한다.
"""


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))


print(solution([0, 0, 0]))

