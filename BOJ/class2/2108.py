"""
- BOJ 2108
- CDR
- 빈도 수 구할 때는 collections 패키지의 Counter 모듈을 사용하자.
"""
import sys
from collections import Counter


def num_avg(arr, num):
    return sum(arr) / num


def center(arr, num):
    return arr[num // 2]


def mode(arr):
    cnt = Counter(arr).most_common()    # Counter 함수: 빈도수 계산, most_common 함수: 빈도수 기준으로 정렬시켜줌
    print(cnt)
    if len(cnt) > 1:    # 빈도 수가 있는 값이 하나만 존재할 경우( ex. arr 가 3,3,3일 경우 )
        if cnt[0][1] == cnt[1][1]:  # 최빈 값이 2개 이상일 경우
            return cnt[1][0]    # 최빈 값중 2번째로 작은 값
        else:
            return cnt[0][0]
    else:
        return cnt[0][0]


def max_min(arr):
    return arr[-1] - arr[0]     # 정렬되었기에 마지막과 첫번째 값을 비교한다.


n = int(sys.stdin.readline())
array = list()

for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

print("%.f" % (num_avg(array, n)))   # 소수점 1번째자리
print(center(array, n))
print(mode(array))
print(max_min(array))
