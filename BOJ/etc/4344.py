t = int(input())
for _ in range(t):
    array = list(map(int, input().split()))
    avg = sum(array[1:])//array[0]
    cnt = 0
    for i in range(1, len(array)):
        if array[i] > avg:
            cnt += 1
    result = "{:.3f}%".format(cnt/array[0]*100)
    print(result)
