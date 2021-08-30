def solution(dirs):
    direction = {'U': [0, -1], 'L': [-1, 0], 'R': [1, 0], 'D': [0, 1]}
    road = set()    # 중복 제거 함수
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + direction[i][0], y + direction[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            road.add((x, y, nx, ny))    # 출발지, 도착지
            road.add((nx, ny, x, y))    # 도착지, 출발지
            x, y = nx, ny
    return len(road) // 2   # 출발, 도착 그리고 도착, 출발 2개를 넣었기 때문에


def fail_solution(dirs):    # 에제는 통과했지만, 체점시 30점..
    graph = [[0] * 11 for _ in range(11)]
    direction = {'U': [0, -1], 'L': [-1, 0], 'R': [1, 0], 'D': [0, 1]}
    x, y = [5, 5]
    result = 0
    nx, ny = 0, 0
    for i in dirs:
        _x, _y = direction[i]
        nx = x + _x
        ny = y + _y
        if 0 <= nx < 11 and 0 <= ny < 11:
            if graph[x][y] == 0:
                graph[x][y] = 1
                result += 1
            x = nx
            y = ny
    return result


print(solution("LULLLLLLU"))
