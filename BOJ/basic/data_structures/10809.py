import sys
input = sys.stdin.readline
S = input().rstrip()
seq = [-1] * 26
for i in range(len(S)):
    if seq[ord(S[i]) - ord('a')] == -1:
        seq[ord(S[i]) - ord('a')] = i
for j in seq:
    print(j, end=' ')
