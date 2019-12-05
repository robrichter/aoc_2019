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
        self.distance = SIZE_X
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
        for instruction in instructions:
            for _ in range(instruction['steps']):
                self.go[instruction['direction']]()
                self.plan[self.position.y][self.position.x] = 1

    def set_distance(self, instructions):
        self.position.x, self.position.y = START_X, START_Y
        for instruction in instructions:
            for _ in range(instruction['steps']):
                self.go[instruction['direction']]()
                if self.plan[self.position.y][self.position.x]:
                    distance = abs(self.start.x - self.position.x) + abs(self.start.y - self.position.y)
                    if distance < self.distance:
                        self.distance = distance


plan = Plan()
plan.draw_wire(wires[0])
plan.set_distance(wires[1])

puzzle.answer_a = plan.distance
print(plan.distance)

