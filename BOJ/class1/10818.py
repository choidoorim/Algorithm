def my():
    n = int(input())
    min_value = 1000001
    max_value = 0

    array = list(map(int, input().split()))

    for i in range(n):
        if array[i] < min_value:
            min_value = array[i]
        if array[i] > max_value:
            max_value = array[i]

    print('{} {}'.format(min_value, max_value))


n = int(input())
array = list(map(int, input().split()))
print('{} {}'.format(min(array), max(array)))
