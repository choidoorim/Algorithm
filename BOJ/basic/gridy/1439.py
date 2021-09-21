word = input()
count = 0
# 1 과 0 이 바뀌는 시점을 찾아서 // 2, //2 + 1 를 해준다.
# 11001100 일 경우 10, 01, 10 에서 바뀐다.
for i in range(len(word) - 1):
    if word[i] != word[i + 1]:
        count += 1

# 홀수 일 경우 //2 + 1, 짝수 일 경우 //2
print(count // 2 if count % 2 == 0 else (count // 2) + 1)
