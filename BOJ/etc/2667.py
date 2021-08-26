n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if array[x][y] == 1:
        global count
        count += 1
        array[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


room_cnt = []
apt_cnt = 0
count = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            room_cnt.append(count)
            count = 0
            apt_cnt += 1
print(apt_cnt)
room_cnt.sort()
for room in room_cnt:
    print(room)
