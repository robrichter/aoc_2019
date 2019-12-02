import operator

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=2)
puzzle_input = puzzle.input_data.split(',')
intcode = list(map(int, puzzle_input))

INIT = (12, 2)
STEP = 4
END = 99
COUNT = len(intcode)

intcode[1], intcode[2] = INIT

operations = {
    1: operator.add,
    2: operator.mul,
}

for i in range(0, COUNT, STEP):
    if intcode[i] == END:
        break

    opcode_id = intcode[i]
    input1_index = intcode[i + 1]
    input2_index = intcode[i + 2]
    output_index = intcode[i + 3]
    intcode[output_index] = operations[opcode_id](intcode[input1_index], intcode[input2_index])

puzzle.answer_a = intcode[0]
