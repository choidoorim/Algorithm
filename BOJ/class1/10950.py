t = int(input())
result_array = [0] * t

for i in range(t):
    a, b = map(int, input().split())
    result_array[i] = a + b

for i in result_array:
    print(i)
