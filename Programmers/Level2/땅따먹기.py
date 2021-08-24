"""
- Programmers - 땅따먹기
- CDR
- 2차원 배열에서 행 별로 자기 자신을 제외 한 최댓값을 더하는 방식으로 풀이를 진행했습니다.
"""


def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j+1:])  # 자기 자신을 제외 한 수를 더한다.
    return max(land[len(land) - 1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
