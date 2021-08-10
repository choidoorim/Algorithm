def solution(strings, n):
    strings.sort(key=lambda x:(x[n], x))    # index 기준으로 정렬 후, 사전 순으로 정렬
    return strings


print(solution(["abce", "abcd", "cdx"], 2))
