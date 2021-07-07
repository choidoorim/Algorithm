n = int(input())
string = input()

array = []
for i in string:
    array.append(ord(i) - 96)

result = 0
for i in range(n):
    result += (array[i] * 31**i)

print(result % 1234567891)
