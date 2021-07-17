from sys import stdin
x = int(stdin.readline())

array = [0] * 30001     # 결과 값을 저장할 배열

for i in range(2, x + 1):   # i 값 부터 1까지 만들기 위한 최솟 값의 결과를 저장한다
    array[i] = array[i - 1] + 1     # 현재의 수에서 1을 빼는 경우
    # 위에서 저장했던 현재의 수에서 1을 빼는 경우와 2, 3, 5로 나눈 값의 최솟 값을 비교하여 저장
    if i % 2 == 0:
        array[i] = min(array[i], array[i // 2] + 1)
    elif i % 3 == 0:
        array[i] = min(array[i], array[i // 3] + 1)
    elif i % 5 == 0:
        array[i] = min(array[i], array[i // 5] + 1)

print(array[x])
