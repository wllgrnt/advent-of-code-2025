def day7(input_str: str) -> tuple[int, int]:
    """
    Input describes a beam start point and
    the coordinates of beam splitters. The beam
    moves downwards until it hits a splitter, at which
    point it splits.

    Return the number of splits.
    """
    beam_locations = set()
    part_1_split_count = 0 # just the number of times a splitter is hit
    split_count = 0
    for line in input_str.split('\n'):
        if not beam_locations:  # parse line 1
            beam_locations.add(line.index('S'))
        new_beam_locations = set()
        for i, char in enumerate(line):
            if char == '^' and i in beam_locations:
                part_1_split_count += 1
                beam_locations.discard(i)
                for delta in (-1, +1):
                    new_split_loc = i + delta
                    if 0 <= new_split_loc < len(line) and new_split_loc not in new_beam_locations:
                        new_beam_locations.add(new_split_loc)
                        split_count += 1
        beam_locations.update(new_beam_locations)

    return part_1_split_count, 0



if __name__ == "__main__":

    test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    assert day7(test_input) == (21,0)
    with open('inputs/day07.txt') as flines:
        input_str = flines.read()

    print("day 7: ", day7(input_str))

