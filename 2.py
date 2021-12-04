# 백준 1740
def solution(n):
    answer = 0
    binary = bin(int(n))[2:]
    binary_len = len(binary)

    for i in range(binary_len):
        if int(binary[i]) == 1:
            print(binary,binary[i], binary_len - i - 1)
            answer += 3 ** (binary_len - i - 1)     # 3**3, 3**2...
    return answer


print(solution(11))
