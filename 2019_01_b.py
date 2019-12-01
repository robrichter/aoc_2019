from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=1)

data = puzzle.input_data.split('\n')


def count_sum_with_fuel(weight):
    fuel_weight = weight//3-2
    if fuel_weight > 0:
        return fuel_weight + count_sum_with_fuel(fuel_weight)
    return 0


puzzle.answer_b = sum([count_sum_with_fuel(int(x)) for x in data])
print(puzzle.answer_b)

