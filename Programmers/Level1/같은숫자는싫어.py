"""
- Programmers - 같은 숫자는 싫어
- CDR
"""


def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:      # 이전 값과 다른 경우 결과에 대입
            answer.append(arr[i])
    return answer


print(solution([1,1,3,3,0,1,1]))
