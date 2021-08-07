"""
- Programmers - 최대공약수, 최소공배수
- CDR
- 최대공약수는 호클리드호제법을 사용.
- 최소 공배수는 (num1, num2) / 최대공약수
"""


def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def solution(n, m):
    answer = []
    answer.append(int(gcd(m, n)))
    answer.append((n*m) // answer[0])
    return answer


print(solution(3, 12))
