"""
- Programmers - 신규 아이디 추천
- CDR
"""
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


def solution(new_id):
    answer = ''
    # 1
    answer = new_id.lower()
    # 2
    for i in answer:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            continue
        else:
            answer = answer.replace(i, '')
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    answer = list(answer)
    if len(answer) > 0 and answer[-1] == '.':
        del answer[-1]
    if len(answer) > 0 and answer[0] == '.':
        del answer[0]
    # 5
    if len(answer) == 0:
        answer.append('a')
    # 6
    while len(answer) >= 16:
        del answer[-1]
        if len(answer) > 0 and answer[-1] == '.':
            del answer[-1]
    # 7
    while len(answer) < 3:
        answer.append(answer[-1])
    return "".join(answer)


print(solution("abcdefghijklmn.p"))
