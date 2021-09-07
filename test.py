def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        num = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != num:
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return
        answer[num] += 1
    comp(0, 0, N)
    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
