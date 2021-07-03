test_count = int(input())
new_text = ''
new_text_list = []

for i in range(test_count):
    repeat_count, text = input().split()
    for j in range(len(text)):
        new_text += text[j] * int(repeat_count)
    new_text_list.append(new_text)
    new_text = ''

for i in new_text_list:
    print(i)
