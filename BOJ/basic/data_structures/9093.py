from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    word = list(input().split())
    for i in range(len(word)):
        word[i] = word[i][::-1]
    print(' '.join(word))
