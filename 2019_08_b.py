from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=8)

pixels = puzzle.input_data
COLUMNS = 25
ROWS = 6
PIXELS_IN_LAYER = COLUMNS * ROWS
LAYER_COUNT = len(pixels)//PIXELS_IN_LAYER

draw = {'0': ' ', '1': '#'}

for i in range(PIXELS_IN_LAYER):
    for j in range(LAYER_COUNT):
        pixel = pixels[i+j*PIXELS_IN_LAYER]
        if pixel in ('0', '1'):
            print(draw[pixel], end='')
            break
    if not (i + 1) % COLUMNS:
        print()


puzzle.answer_b = 'LEGJY'

