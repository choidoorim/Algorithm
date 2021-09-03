import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(i + 1,a+b))
