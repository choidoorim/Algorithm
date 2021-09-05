n = int(input())
for _ in range(n):
    word = list(input())
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i] in word[i + 1:]:     # 만약 현재 위치 단어가 뒤에 또 있다면
                n -= 1
                break
print(n)
