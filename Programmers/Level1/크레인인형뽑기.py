# 남아있는 바구니의 인형개수를 return 하는 줄 알고 시간을 버렸다.. 문제를 꼼꼼히 읽어봐야겠다ㅠㅜ


def solution(board, moves):
    answer = 0
    pocket = list()
    new_board = [[] for _ in range(len(board))]
    # 크레인 위치에 대한 새로운 board 생성
    for bd in board:
        for i in range(len(board)):
            if bd[i] != 0:
                new_board[i].append(bd[i])
    for move in moves:
        now = 0
        if new_board[move - 1]:     # 크레인의 위치에 인형이 존재한다면
            now = new_board[move - 1][0]
            del new_board[move - 1][0]
        if now != 0:    # 뽑은 인형이 존재한다면
            if pocket and pocket[-1] == now:    # 바구니에 인형이 존재하고, 바구니의 맨 위의 값과 뽑은 값이 일치한다면
                del pocket[-1]
                answer += 2     # 제거된 인형의 개수, 인형은 2개씩 없어지기때문에 +2
            else:
                pocket.append(now)
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
