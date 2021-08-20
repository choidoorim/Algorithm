def solution(numbers, hand):
    answer = ''
    # 좌표 값 저장
    dic = {1:[0, 0], 2:[0, 1], 3:[0, 2],
           4:[1, 0], 5:[1, 1], 6:[1, 2],
           7:[2, 0], 8:[2, 1], 9:[2, 2],
           '*':[3, 0], 0:[3, 1], '#':[3, 2]}
    left_now = dic['*']
    right_now = dic['#']
    for num in numbers:
        if num in [1, 4, 7]:
            left_now = dic[num]
            answer += 'L'
        elif num in [3, 6, 9]:
            right_now = dic[num]
            answer += 'R'
        else:
            current = dic[num]
            # 유클리드 거리 측정 법 abs(a1 - b1) + abs(a2 - b2)
            left = abs(current[0] - left_now[0]) + abs(current[1] - left_now[1])
            right = abs(current[0] - right_now[0]) + abs(current[1] - right_now[1])
            if left > right:
                answer += 'R'
                right_now = dic[num]
            elif left < right:
                answer += 'L'
                left_now = dic[num]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_now = dic[num]
                else:
                    answer += 'L'
                    left_now = dic[num]
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
