a = input()
b = input()
c = input()

sum_result = int(a) * int(b) * int(c)

array = [0] * 10
sum_result = str(sum_result)
for i in sum_result:
    array[int(i)] += 1

for i in range(len(array)):
    print(array[i])
