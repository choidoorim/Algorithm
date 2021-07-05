n = int(input())

sum_num = 1
num = 6
room = 1

while True:
    if n <= sum_num:
        print(room)
        break
    num = 6 * room
    sum_num += num
    room += 1

