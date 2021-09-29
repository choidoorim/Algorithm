S = list(input())
result = []
while S:
    result.append(''.join(S))
    del S[0]
result.sort()
for i in result:
    print(i)