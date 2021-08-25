# 접두어란 맨 앞에 붙이는 말,
# 정렬을 하면 접두어 일 경우 붙어있게 된다. 따라서 현재와 다음 문자열을 비교해서 접두어를 찾는다.
# 현재 문자와 뒤 배열의 문자 중 현재문자의 길이 만큼만 비교한다. 접두어는 앞에 있는 것이니깐
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:   #
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
