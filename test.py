import math


def solution(n, words):
    answer = []
    success_words = [words[0]]
    success_status = True
    a, b = 0, 0
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0]:
            a = math.ceil((i + 1) / n)
            if (i + 1) % n == 0:
                b = n
            else:
                b = (i + 1) % n
            answer = [b, a]
            success_status = False
            break
        if words[i] in success_words:
            a = math.ceil((i + 1) / n)
            if (i + 1) % n == 0:
                b = n
            else:
                b = (i + 1) % n
            answer = [b, a]
            success_status = False
            break
        else:
            success_words.append(words[i])
    if success_status:
        answer = [0, 0]
    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
