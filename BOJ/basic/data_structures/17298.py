import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
""" 시간 초과
result = []
for i in range(len(A)):
    num = 0
    for j in range(i, len(A)):
        if A[i] < A[j]:
            num = A[j]
            break
        else:
            num = -1
    result.append(str(num))
print(' '.join(result))
"""
result = [str(-1)] * N  # 오큰수를 못찾을 경우 -1 출력
stack = []      # 인덱스를 저장
for i in range(len(A)):
    # 스택에 값이 존재하고, 스택 상단의 인덱스에 해당하는 값보다 인덱스 i의 값이 클 경우
    while stack and A[stack[-1]] < A[i]:
        print(i, result)
        result[stack.pop()] = str(A[i])
    stack.append(i)
print(' '.join(result))
