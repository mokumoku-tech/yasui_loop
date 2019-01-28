# coding: utf-8

import sys
import random
import time

print('文字列を入力して下さい => ', end = '')
input_word = input()

if len(input_word) > 8:
    okay = False
    while not okay:
        while True:
            if len(input_word) > 10:
                print('めっちゃ', end = '')
            print('時間かかるかも知れないけどいいの？[y/n]')
            yes_or_no = input()
            if yes_or_no in { 'y', 'n' }:
                break
        if yes_or_no == 'y':
            okay = True
        if yes_or_no == 'n':
            print('Good call!')
            sys.exit()

for_count = 0
is_input_word = False
start = time.time()
while not is_input_word:
    for_count += 1
    i = 0
    result = ''
    chars = [*input_word]
    numbers = [*range(0, len(input_word))]

    for _ in range(len(chars)):
        random_number = random.randint(0, len(numbers) - 1)
        result = result + chars[random_number]
        chars.pop(random_number)
        numbers.pop(random_number)

    print(result)

    if result == input_word:
        is_input_word = True
elapsed_time = time.time() - start
print('')
print('Congratulation!')
print('「%s」が生成されるまで%f秒かかり、%s回ループしました' % (input_word, elapsed_time, for_count))
