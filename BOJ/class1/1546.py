a = int(input())
score = list(map(int, input().split()))
big_num = max(score)
score_sum = 0

for i in range(a):
    score[i] = score[i]/big_num*100

for i in range(a):
    score_sum += score[i]

print(score_sum/a)
