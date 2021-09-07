import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
new_array = sorted(list(set(array)))
# for i in range(n):
#     print(new_array.index(array[i]), end=' ')
dic = {new_array[i]:i for i in range(len(new_array))}
for i in array:
    print(dic[i], end=' ')
