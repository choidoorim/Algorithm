array = list()

for i in range(10):
    array.append(int(input()))
    array[i] = array[i] % 42

array = set(array)  # 중복 제거 함수

print(len(array))
