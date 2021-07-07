n = int(input())

array = []
for i in range(n):
    m_age, m_name = map(str, input().split())
    array.append((int(m_age), m_name))

array.sort(key=lambda x: x[0])

for m in array:
    print(m[0], m[1])
