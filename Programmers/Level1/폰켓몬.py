"""
- Programmers - 폰켓몬
- CDR
- dictionary 를 사용하여 배열내 종류를 알 수 있도록 사용했고,
  N/2 만큼 가져갈 수 있으니 dictionary 안에 종류가 N/2 이거나 그것보다 클 경우는 N/2 return,아닐 경우는 dictionary 의 종류만큼 return
"""


def solution(nums):
    dic = dict()
    mid = len(nums) // 2
    for num in nums:
        if num not in dic:
            dic[num] = 0
        else:
            continue
    if len(dic) >= mid:
        return mid
    else:
        return len(dic)


print(solution([3,3,3,2,2,4]))
