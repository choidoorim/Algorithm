n = int(input())

score_array = []
sum_score = [0] * n

for i in range(n):
    score = input()
    count = 0
    for j in score:
        if j == 'O':
            count += 1
            sum_score[i] += count
        else:
            count = 0

for i in sum_score:
    print(i)
