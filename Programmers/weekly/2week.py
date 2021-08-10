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


def solution(scores):
    answer = ''
    for i in range(len(scores)):
        new_array = list()
        my_score = 0
        for j in range(len(scores)):
            new_array.append(scores[j][i])
            if j == i:
                my_score = scores[j][i]
        if (min(new_array) == my_score or max(new_array) == my_score) and new_array.count(my_score) == 1:
            del new_array[i]
        print(new_array)
        total = sum(new_array) / len(new_array)
        answer += find_grade(total)
    return answer


print(solution(	[[75, 50, 100], [75, 100, 20], [100, 100, 20]]))