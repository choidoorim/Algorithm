import sys
n = int(sys.stdin.readline())

sum_one = 0
sum_two = 0

array = list()
for _ in range(n):
    array.append(sys.stdin.readline().rstrip())

for i in array[0]:
    print(i)
