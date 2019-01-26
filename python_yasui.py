# coding: utf-8

import random

for_count = 0
is_not_yasui = True

while is_not_yasui:
    for_count += 1
    i = 0
    result = ''
    chars = ['パ', 'イ', 'ソ', 'ン', 'や', 'す', 'い']
    numbers = [0, 1, 2, 3, 4, 5, 6]

    for _ in range(len(chars)):
        random_number = random.randint(0, len(numbers) - 1)
        result = result + chars[random_number]
        chars.pop(random_number)
        numbers.pop(random_number)

    print(result)

    if result == 'パイソンやすい':
        is_not_yasui = False
        print('')
        print('Congratulation!')
        print('「パイソンやすい」が生成されるまで%s回ループしました' % for_count)

