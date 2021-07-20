test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = [0 for _ in range(n)]
    idx[m] = 1  # target
    count = 0

    while True:
        if imp[0] == max(imp):
            count += 1

            if idx[0] == 1:
                print(count)
                break
            else:
                del imp[0]
                del idx[0]
        else:
            imp.append(imp[0])
            del imp[0]
            idx.append(idx[0])
            del idx[0]
        print(imp)