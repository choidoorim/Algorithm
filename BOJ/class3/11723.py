"""
- BOJ 11723
- CDR
- if x in array: -> array 배열 내에서 x 값 찾기
- clear() method : 배열을 초기화 시킨다
- remove(x) method : 배열
- 시간 초과로 인한 로직 수정
- set 은 중복을 허용하지 않고, 순서가 없다
- remove 메소드는 지우려는 element 가 없을 경우 error 발생 하지만,
  discard 메소드는 지우려는 element 가 없어도 정상 종료 한다
"""
# from sys import stdin
#
# m = int(stdin.readline())
# S = []
#
#
# def add_x(num):
#     if num not in S:
#         S.append(num)
#
#
# def remove_x(num):
#     if num in S:
#         S.remove(num)
#
#
# def check(num):
#     if num in S:
#         print(1)
#     else:
#         print(0)
#
#
# def toggle(num):
#     if num in S:
#         S.remove(num)
#     elif num not in S:
#         S.append(num)
#
#
# def all_x():
#     S.clear()
#     for i in range(1, 21):
#         S.append(i)
#
#
# def empty():
#     S.clear()
#
#
# for _ in range(m):
#     command = list(stdin.readline().split())
#     if command[0] == 'add':
#         add_x(int(command[1]))
#     elif command[0] == 'remove':
#         remove_x(int(command[1]))
#     elif command[0] == 'check':
#         check(int(command[1]))
#     elif command[0] == 'toggle':
#         toggle(int(command[1]))
#     elif command[0] == 'all':
#         all_x()
#     elif command[0] == 'empty':
#         empty()
#     print(S)
#
# collect
from sys import stdin

m = int(stdin.readline())

S = set()   # set 함수는 집합 때 사용
for _ in range(m):
    command = list(stdin.readline().split())
    if len(command) == 1:
        if command[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:   # empty
            S = set()   # 비어있는 set 만들기
    else:
        x = int(command[1])
        if command[0] == 'add':
            S.add(x)
        elif command[0] == 'remove':
            S.discard(x)
        elif command[0] == 'check':
            print(1 if x in S else 0)
        else:   # toggle
            S.discard(x) if x in S else S.add(x)
