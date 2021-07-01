# 참고: https://wook-2124.tistory.com/257
a = input().lower()     # 소문자로 변경
a_list = list(set(a))   # 중복 제거
cnt = []    # 알파벳 개수 배열

for i in a_list:
    cnt_word = a.count(i)   # 알파벳의 개수를 계산
    cnt.append(cnt_word)    # 개수 배열에 추가


if cnt.count(max(cnt)) >= 2:    # max() 메소드를 통해 최대 값이 여러개일 경우 ? 출력
    print('?')
else:   # 아닐 경우 제일 큰 값의 알파벳을 대문자로 출력
    print(a_list[cnt.index(max(cnt))].upper())
