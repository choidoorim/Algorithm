"""
- BOJ 1966
- CDR
"""
from sys import stdin
test_count = int(stdin.readline())
for _ in range(test_count):
    n, m = map(int, stdin.readline().split())
    imp = list(map(int, stdin.readline().split()))
    idx = [0 for _ in range(n)]  # target 에 대한 list
    idx[m] = 1  # target

    count = 0   # 순서

    while True:
        if imp[0] == max(imp):  # 1. 중요도를 확인하여 중요도가 높은 것일 경우
            count += 1

            if idx[0] == 1:  # 궁금한 문서 일 경우
                print(count)
                break
            else:   # 궁금한 문서가 아닐 경우 - 인쇄
                del imp[0]
                del idx[0]
        else:  # 중요도가 높은 것이 아닐 경우 - 배열 뒤로 배치
            imp.append(imp[0])
            del imp[0]
            idx.append(idx[0])
            del idx[0]
