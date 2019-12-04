import numpy as np

from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=3)
wires = puzzle.input_data.split('\n')
wires = [[{'direction': path[:1], 'steps': int(path[1:])} for path in wire.split(',')] for wire in wires]

SIZE_X = SIZE_Y = 40000
START_X, START_Y = SIZE_X//2, SIZE_Y//2

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x:{self.x} y:{self.y}"


class Plan:
    def __init__(self):
        self.plan = np.zeros((SIZE_X, SIZE_Y), dtype=int)
        self.start = Coords(START_X, START_Y)
        self.position = Coords(START_X, START_Y)
        self.intersections = set()
        self.steps = SIZE_X * SIZE_Y
        self.go = {'U': self.up,
                   'D': self.down,
                   'R': self.right,
                   'L': self.left}

    def up(self):
        self.position.y -= 1

    def down(self):
        self.position.y += 1

    def right(self):
        self.position.x += 1

    def left(self):
        self.position.x -= 1

    def draw_wire(self, instructions):
        steps = 0
        for instruction in instructions:
            for _ in range(instruction['steps']):
                self.go[instruction['direction']]()
                steps += 1
                self.plan[self.position.y][self.position.x] = steps

    def set_intersections(self, instructions):
        self.position.x, self.position.y = START_X, START_Y
        steps = 0
        for instruction in instructions:
            for _ in range(instruction['steps']):
                self.go[instruction['direction']]()
                steps += 1
                position_value = self.plan[self.position.y][self.position.x]
                if position_value:
                    steps_sum = steps + position_value
                    if self.steps > steps_sum:
                        self.steps = steps_sum


plan = Plan()
plan.draw_wire(wires[0])
plan.set_intersections(wires[1])

print(plan.steps)
puzzle.answer_b = plan.steps
