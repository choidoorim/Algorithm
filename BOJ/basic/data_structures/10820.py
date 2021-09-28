import sys
while True:
    line = sys.stdin.readline().rstrip('\n')
    result = [0] * 4
    if not line:
        break

    for i in line:
        if i.islower():
            result[0] += 1
        elif i.isupper():
            result[1] += 1
        elif i.isdigit():
            result[2] += 1
        elif i == ' ':
            result[3] += 1
    print(' '.join(map(str, result)))
