from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=8)

pixels = puzzle.input_data
COLUMNS = 25
ROWS = 6
PIXELS_COUNT = COLUMNS * ROWS


def get_count(index, value):
    return pixels[index:index + PIXELS_COUNT].count(value)


counts = []
for i in range(0, len(pixels), PIXELS_COUNT):
    counts.append({'0': get_count(i, '0'),
                   '1': get_count(i, '1'),
                   '2': get_count(i, '2')})

fewest = min(counts, key=lambda x: x['0'])
puzzle.answer_a = fewest['1'] * fewest['2']
