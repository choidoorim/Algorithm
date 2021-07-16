n = input()
m = input()

for i in range(len(m) - 1, -1, -1):
    print(int(n) * int(m[i]))
print(int(n) * int(m))

