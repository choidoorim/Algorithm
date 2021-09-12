i = 1
while True:
    # P일 중 L 일만 사용가능, 강산이는 V 일짜리 휴가 시작
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    result = (V // P) * L      # P 일중 L일을 모두 사용할 수 있는 경우
    if (V % P) > L:     # P 일중 L일을 모두 사용하지 못하는 나머지 경우
        result += L
    else:
        result += (V % P)
    print("Case {}: {}".format(i, result))
    i += 1

