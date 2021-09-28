import sys
input = sys.stdin.readline
S = input().rstrip()
en = [0] * 26
for i in S:
    en[ord(i) - ord('a')] += 1
for j in en:
    print(j, end=' ')