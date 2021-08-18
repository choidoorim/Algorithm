# zip(a, b) : a, b 배열의 공통되는 것을 짝지어 준다.
from collections import Counter


# Counter 를 사용한 풀이 방법
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]


def my_solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]  # 비교했을 때 모두 같다면 당연히 마지막에 있는 이름이 완주하지 못한 이름이다.


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
