# coding: utf-8

import random

print('文字列を入力して下さい => ', end = '')
input = input()

for_count = 0
is_not_input_word = True

while is_not_input_word:
    for_count += 1
    i = 0
    result = ''
    chars = [*input]
    numbers = [*range(0, len(input))]

    for _ in range(len(chars)):
        random_number = random.randint(0, len(numbers) - 1)
        result = result + chars[random_number]
        chars.pop(random_number)
        numbers.pop(random_number)

    print(result)

    if result == input:
        is_not_input_word = False
        print('')
        print('Congratulation!')
        print('「%s」が生成されるまで%s回ループしました' % (input, for_count))
