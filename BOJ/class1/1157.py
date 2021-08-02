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
