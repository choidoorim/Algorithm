array = list(map(int, input().split()))
status = ''

if array == sorted(array):
    print('ascending')
elif array == sorted(array, reverse=True):
    print('descending')
else:
    print('mixed')
