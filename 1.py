# 구현 문제
def solution(N, tree):
    # x 가 가장 작은 애가 중심.
    answer = 1
    tree.sort()
    x, y = tree[0]

    # 정렬 시 x 는 커지고 y 가 작아지는 순간이 경계가 발생.
    # y 가 커지면 이미 구역안에 존재한다.
    for i in range(1, len(tree)):
        if tree[i][0] > x and tree[i][1] < y:
            answer += 1
            x, y = tree[i]

    return answer


print(solution(5, [[4, 3], [3, 1], [2, 2], [1, 4]]))
# [[3, 3], [2, 2], [1, 1]]
# [[4, 3], [3, 1], [2, 2], [1, 4]]