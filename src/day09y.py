import numpy as np


def rectangle_valid(x1, y1, x2, y2, red_coords):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    n = len(red_coords)
    for i in range(n):
        ex1, ey1 = red_coords[i]
        ex2, ey2 = red_coords[(i + 1) % n]

        if ex1 == ex2:  # vertical edge
            if min_x < ex1 < max_x:  # strictly inside rect's x-range
                edge_ymin, edge_ymax = min(ey1, ey2), max(ey1, ey2)
                if edge_ymin < max_y and edge_ymax > min_y:  # y overlap
                    return False
        else:  # horizontal edge
            if min_y < ey1 < max_y:  # strictly inside rect's y-range
                edge_xmin, edge_xmax = min(ex1, ex2), max(ex1, ex2)
                if edge_xmin < max_x and edge_xmax > min_x:  # x overlap
                    return False
    return True

def day9(input_str: str) -> tuple[int, int]:
    """<input_str> lists red tile coodinates in a grid - find the largest rectangle that uses red tiles for two opposite corners."""
    # ie the furthest distance two points, where distance here is the rectangle size, square of the l1 distance.
    coords = np.asarray([line.split(',') for line in input_str.split('\n') if line.strip()], dtype=int)
    dx = np.abs(coords[:, np.newaxis, 0] - coords[np.newaxis, :, 0])
    dy = np.abs(coords[:, np.newaxis, 1] - coords[np.newaxis, :, 1])
    areas = (dx+1) * (dy+1)

    # part 2: the red tiles are connected by green tiles, and the tiles inside this loop are also green.
    # find the largest rectangle that's inside this area.
    # ie there are no red tiles within the inner boundary of the rectangle.
    part1_max = areas.max()
    i, j = np.triu_indices(len(areas), k=1)
    upper_areas = areas[i, j]
    order = np.argsort(-upper_areas)  # negative for descending

    for idx in order:
        p1, p2 = i[idx], j[idx]
        x1, y1 = coords[p1]
        x2, y2 = coords[p2]

        if rectangle_valid(x1, y1, x2, y2, coords):
            part2_max = upper_areas[idx]
            return part1_max, part2_max





if __name__ == "__main__":

    test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    assert day9(test_input,) == (50,24)
    with open('input/day09.txt') as flines:
        input_str = flines.read()

    print("day 9: ", day9(input_str))


