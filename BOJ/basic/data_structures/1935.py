n = int(input())
postfix = list(input())
nums = []
for i in range(n):
    nums.append(int(input()))
stack = []

for i in postfix:
    if i.isalpha():
        stack.append(nums[ord(i) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '/':
            stack.append(num1 / num2)
        else:
            stack.append(num1 * num2)
print('{:.2f}'.format(stack[0]))
