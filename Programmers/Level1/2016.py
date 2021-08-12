"""
- Programmers - 2016
- CDR
- datetime module 을 사용해서 요일을 출력하자. 결과 0 - 월요일, 1 - 화요일 ...
"""
import datetime


def solution(a, b):
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return day[datetime.date(2016, a, b).weekday()]


print(solution(5, 24))
