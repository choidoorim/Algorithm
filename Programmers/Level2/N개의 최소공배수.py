# 처음부터 끝까지 차례대로 최소공배수를 누적시키며 계산하면 된다.


def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


def solution(arr):
    arr.sort()
    result = arr[0]
    for i in range(1, len(arr)):
        result = result * arr[i] // gcd(result, arr[i])
    return result


print(solution([2, 6, 8, 14]))
