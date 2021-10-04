import sys
input = sys.stdin.readline


array = list(input().rstrip())
result = []


def list_chuck(arr, n):     # 8 진수로 변환해야하기 때문에 배열을 3개로 분할
    return [arr[i: i + n] for i in range(0, len(arr), n)]


array.reverse()       # 뒤에서부터 계산하기 위해서 배열을 거꾸로 바꿈.
array = list_chuck(array, 3)
for i in array:
    res = 0
    for j in range(len(i)):
        if i[j] == '1':
            res += 2 ** j
    result.append(str(res))

result.reverse()    #
print(''.join(result))
