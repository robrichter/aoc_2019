from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=4)
MIN, MAX = tuple(map(int, puzzle.input_data.split('-')))

passwords = 0
for number in range(MIN, MAX+1):
    numbers = str(number)
    numbers = list(numbers)
    old_digit = numbers[0]
    is_valid = False
    for digit in numbers[1:]:
        if old_digit == digit:
            is_valid = True
            old_digit = digit
            continue
        if old_digit > digit:
            is_valid = False
            break
        old_digit = digit

    if is_valid:
        passwords += 1


puzzle.answer_a = passwords

