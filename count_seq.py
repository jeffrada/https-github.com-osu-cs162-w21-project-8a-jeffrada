# Author: Adam Jeffries
# Date: 2/24/2021
# Description: A generator function named count_seq that doesn't take any parameters and generates a given sequence.

def count_seq():
    """
    A function that yields indefinite terms of the count sequence.
    """
    current_step = '2'
    while True:
        yield current_step
        number = '0'
        count = 0
        next_step = ''
        for num in current_step:
            if num != number:
                if count != 0:
                    next_step += str(count)
                    next_step += number
                number = num
                count = 1
            else:
                count = count + 1
        next_step += str(count)
        next_step += number
        current_step = next_step
