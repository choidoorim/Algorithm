"""
- Programmers - 최솟값 만들기
- CDR
- A 배열의 제일 작은 값과 B 배열의 제일 큰 값을 골라 곱하면 최솟 값을 구할 수 있습니다.
"""


def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


print(solution([1, 4, 2], [5, 4, 4]))
