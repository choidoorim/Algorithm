def solution(n, lost, reserve):
    # 여벌 체육복이 있지만 도난당한 친구가 있을 수도 있기 때문에 set 함수로 중복 제거
    reserve_s = set(reserve) - set(lost)
    lost_s = set(lost) - set(reserve)
    
    n -= len(lost_s)    # 체육복을 소지한 학생의 수
    for i in lost_s:
        if i - 1 in reserve_s:
            reserve_s.remove(i - 1)
            n += 1
        elif i + 1 in reserve_s:
            reserve_s.remove(i + 1)
            n += 1
    return n


print(solution(5, [2, 4], [3]))
