import numpy as np


def is_accessible(input_arr, index):
    neighbour_count = 0
    directions = [(0,1), (1,0), (-1, 0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    i,j = index
    m, n = input_arr.shape
    for delta_i, delta_j in directions:
        neighbour_i, neighbour_j = i + delta_i, j + delta_j
        if 0 <= neighbour_i < m and 0 <= neighbour_j < n and input_arr[neighbour_i, neighbour_j]:
            neighbour_count += 1

    return neighbour_count < 4



def day4(input_str) -> tuple[int, int]:
    """The input string represents a grid of objects (@). An object is only accessible if there are fewer than
    four objects in the eight adjacent positions.
    Part 1: Find the accessible objects
    Part 2: Run a removal process. Iteratively remove accessible rolls. Maintain a count.
    """
    input_arr = np.asarray([[char == '@' for char in line] for line in input_str.split('\n') if line.strip()])

    initial_accesible_count = None
    accessible_count = 0
    while True:
        object_positions = np.argwhere(input_arr)
        accessibles = []
        for object_position in object_positions:
            if is_accessible(input_arr, object_position):
                accessibles.append(object_position)
                accessible_count += 1

        if initial_accesible_count is None:
            initial_accesible_count = accessible_count

        for i, j in accessibles:
            input_arr[i,j] = False

        if not accessibles:
            break

    return initial_accesible_count,accessible_count

test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

assert day4(test_input) == (13, 43)

if __name__ == "__main__":

    with open('inputs/day04.txt') as flines:
        input_str = flines.read()

    print("day 4: ", day4(input_str))

