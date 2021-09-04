word = input()
change_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in change_word:
    word = word.replace(i, 'w')
print(len(word))
