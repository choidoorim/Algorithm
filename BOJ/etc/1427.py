"""
- BOJ 1427
- CDR
"""
array = list(input())
array.sort(reverse=True)
for arr in array:
    print(arr, end='')
