from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=1)

data = puzzle.input_data.split('\n')

puzzle.answer_a = sum([int(x)//3-2 for x in data])
