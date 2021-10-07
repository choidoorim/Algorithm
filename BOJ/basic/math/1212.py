import sys
input = sys.stdin.readline
n = input()
answer = ''
for i in range(len(n) - 1, -1, -1):
    num = int(n[i])
    result = ''
    while num > 0:
        result += str((num % 2))
        num = num // 2
    if i != 0:
        while 3 > len(result):
            result += '0'
    answer += result
if not answer:
    print(0)
else:
    print(answer[::-1])
