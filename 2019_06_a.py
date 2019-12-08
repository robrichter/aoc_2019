from aocd.models import Puzzle


puzzle = Puzzle(year=2019, day=6)
input_data = puzzle.input_data
# input_data = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"


class Node:
    def __init__(self, child):
        self.children = [child]
        self.children_count = 1

    def append_child(self, child):
        self.children.append(child)
        self.children_count += 1


tree = {}

for line in input_data.split('\n'):
    parent, child = line.split(')')
    if tree.get(parent):
        tree[parent].append_child(child)
    else:
        tree[parent] = Node(child)


def get_children_count(node):
    count_sum = node.children_count
    for child in node.children:
        if tree.get(child):
            count_sum += get_children_count(tree[child])
    return count_sum


children_sum = 0
for node in tree.values():
    children_sum += get_children_count(node)

print(children_sum)
puzzle.answer_a = children_sum

