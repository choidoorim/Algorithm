import sys
input = sys.stdin.readline
N, B = input().split()
result, cnt = 0, 0
for i in range(len(N) - 1, -1, -1):
    num = int(N[i]) if N[i].isdigit() else ord(N[i]) - 55
    result += (num * (int(B) ** cnt))
    cnt += 1
print(result)
