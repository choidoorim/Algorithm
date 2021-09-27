
"""
후위표기법
1. 연산들과 괄호는 전부 stack 에 넣는다.
2. 닫힘 괄호가 나올 경우 열린 괄호가 나올 떄 까지 stack 에 있는 것들을 모두 차례대로 뺀다.
3. 지금 넣을려는 연산자보다 스택에 담겨있는 연산자의 우선순위가 크거나 같다면
스택에서 연산자를 빼고 결과에 넣어준 뒤에 나머지 연산을 스택에 담는다.
"""
command = input()
stack = []
result = []
prior = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0}
for i in command:
    if i.isalpha():
        result.append(i)
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:   # 연산자 일 경우
            # 우선순위가 낮은 것들을 출력
            while stack and prior[stack[-1]] >= prior[i]:
                result.append(stack.pop())
            stack.append(i)
while stack:
    result.append(stack.pop())
print(''.join(result))
