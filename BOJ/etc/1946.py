"""
- BOJ 1946
- CDR
- 그리디
- 서류 심사 기준으로 정렬시킨 후, 
  1. 1등의 면접 전형을 기준으로 다른 사원의 면접 전형을 비교
  2. 1등의 면접 전형보다 잘 본 사람이 있을 경우 그 사원을 기준으로 면접 전형을 비교
  3. 반복
"""
import sys
t = int(input())
input = sys.stdin.readline
for _ in range(t):
    n = int(input())
    array = []
    cnt = 1
    for _ in range(n):
        dcm, itv = map(int, input().split())
        array.append([dcm, itv])
    array.sort(key=lambda x:x[0])   # 서류 심사 기준으로 정렬
    compare_num = array[0][1]   # 서류 심사 1등의 면접 전형 순위
    for arr in array:
        if compare_num > arr[1]:
            cnt += 1
            compare_num = arr[1]
    print(cnt)
