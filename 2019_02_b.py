import operator

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=2)
puzzle_input = puzzle.input_data.split(',')
init_intcode = list(map(int, puzzle_input))

GOAL = 19690720
ITERATIONS = 100
INIT = (12, 2)
STEP = 4
END = 99
COUNT = len(init_intcode)

operations = {
    1: operator.add,
    2: operator.mul,
}

for j in range(ITERATIONS):
    for k in range(ITERATIONS):
        intcode = init_intcode[:]
        intcode[1] = j
        intcode[2] = k
        for i in range(0, len(intcode), 4):
            if intcode[i] == END:
                break

            opcode_id = intcode[i]
            input1_index = intcode[i + 1]
            input2_index = intcode[i + 2]
            output_index = intcode[i + 3]
            intcode[output_index] = operations[opcode_id](intcode[input1_index], intcode[input2_index])

        if intcode[0] == GOAL:
            puzzle.answer_b = f"{j}{k}"
            break

