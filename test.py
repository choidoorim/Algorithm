array = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
answer = ''


def find_grade(num):
    if num >= 90:
        return 'A'
    elif 80 <= num < 90:
        return 'B'
    elif 70 <= num < 80:
        return 'C'
    elif 50 <= num < 70:
        return 'D'
    else:
        return 'F'


for i in range(len(array)):
    new_array = list()
    my_score = 0
    for j in range(len(array)):
        new_array.append(array[j][i])
        if j == i:
            my_score = array[j][i]
    if (min(new_array) == my_score or max(new_array) == my_score) and new_array.count(my_score) > 0:
        del new_array[i]
    total = sum(new_array) // len(new_array)
    answer += find_grade(total)
print(answer)
