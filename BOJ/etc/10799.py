"""
- 백준: 10799
- stack 사용
"""
laser = input()
stack = []
cnt = 0
bar = 0
for i in range(len(laser)):
    if laser[i] == '(':
        stack.append(laser[i])
        bar += 1
    else:
        bar -= 1
        if stack[-1] == '(':
            stack.pop()
            if laser[i - 1] == '(':     # () 일 경우
                cnt += bar
            else:
                cnt += 1
print(cnt)
