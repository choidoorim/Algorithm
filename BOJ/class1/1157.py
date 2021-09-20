word = input().upper()
alphabet = dict()

for i in word:
    if i in alphabet:
        alphabet[i] += 1
    else:
        alphabet[i] = 1

big_num = 0
big_word = 0
for alpha in alphabet:
    if alphabet[alpha] > big_num:
        big_num = alphabet[alpha]
        big_word = alpha
    elif alphabet[alpha] == big_num:
        big_word = '?'
print(big_word.upper())


def new():
    word = input()
    word = word.lower()
    dic = dict()
    for i in word:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    max_number = max(dic.values())
    result = dict((key, value) for key, value in dic.items() if value == max_number)
    if len(result) == 1:
        answer = list(result.keys())
        print(answer[0].upper())
    else:
        print('?')
