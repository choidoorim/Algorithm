import math


def solution(n, words):
    answer = []
    success_words = [words[0]]  # 정답인 단어를 담을 배열
    success_status = True   # 끝말잇기가 성공적으로 수행됬는지 확인하는 상태 값

    def find_answer(num):   # [사람, 차례]
        # 사람: 지금 현재 위치 % 참가하는 사람, 결과가 0 일 경우는 n 번째 사람의 차례
        # 차례: 올림(지금 현재 위치 / 참가하는 사람)
        return [n if (num + 1) % n == 0 else (num + 1) % n, math.ceil((num + 1) / n)]

    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0]:     # 현재 값의 첫 글자가 전 마지막 글자와 다를 경우
            answer = find_answer(i)
            success_status = False              # 끝말잇기 실패
            break
        if words[i] in success_words:           # 기존에 외쳤던 단어를 다시 외치는 경우
            answer = find_answer(i)
            success_status = False
            break
        else:
            success_words.append(words[i])
    if success_status:                          # 성공적으로 끝말잇기 수행 시
        answer = [0, 0]
    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
