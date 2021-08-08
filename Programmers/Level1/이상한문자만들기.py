"""
- Programmers - 자리수 더하기
- CDR
- split(" ") 으로 해야 함. 테스트 케이스에서 한 개 이상의 공백을 보존하는 것 같기 때문
"""


def solution(s):
    word_list = s.split(' ')
    array = []
    for word in word_list:
        new_word = ''
        for j in range(len(word)):
            if j % 2 == 0:
                new_word += word[j].upper()
            else:
                new_word += word[j].lower()
        array.append(new_word)
    return " ".join(array)


print(solution("try hello world"))
