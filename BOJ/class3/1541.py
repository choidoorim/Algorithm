"""
- BOJ 1541
- CDR
- split 함수를 통해 값을 나눠준다
"""
# 최솟 값을 출력하기 위해서는 - 기준으로 괄호를 나눠줘야한다
data = input().split('-')
num = []
for i in data:
    split_num = i.split('+')    # 괄호로 묶인 값들을 각각 + 연산을 해준다 [55, 50+40, 35+60 ...]
    sum_num = 0
    for j in split_num:
        sum_num += int(j)
    num.append(sum_num)
# 첫 번째 수를 제외한 값들을 모두 더해준다
result = num[0]
for k in range(1, len(num)):
    result -= num[k]
print(result)