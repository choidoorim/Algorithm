import sys
n = int(sys.stdin.readline())
n_array = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

dictionary = dict()    # 키 값과 값의 쌍으로 이루어져있다.

for i in n_array:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

for target in m_array:
    if target in dictionary:
        print(dictionary[target], end=' ')
    else:
        print(0, end=' ')
