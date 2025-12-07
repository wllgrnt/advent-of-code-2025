from collections import Counter

def day7(input_str: str) -> tuple[int, int]:
    """
    Part 1: Count total splits
    Part 2: Count distinct timelines
    """
    beam_locations = set() 
    timeline_counts = Counter()
    part_1_split_count = 0

    for line in input_str.split('\n'):
        if not beam_locations:  # parse line 1
            start_pos = line.index('S')
            beam_locations.add(start_pos)
            timeline_counts[start_pos] = 1
            continue

        new_beam_locations = set()
        new_timeline_counts = Counter()
        splitters_hit = set()

        for i, char in enumerate(line):
            if char == '^' and i in beam_locations:
                splitters_hit.add(i)
                # Part 1: count the split
                part_1_split_count += 1
                beam_locations.discard(i)
                # Part 2: each timeline at position i splits into two
                timelines_here = timeline_counts[i]

                for delta in (-1, +1):
                    new_pos = i + delta
                    if 0 <= new_pos < len(line):
                        new_beam_locations.add(new_pos)
                        new_timeline_counts[new_pos] += timelines_here

        # Timelines that didn't hit a splitter continue straight down
        for pos, count in timeline_counts.items():
            if pos not in splitters_hit:
                new_timeline_counts[pos] += count

        beam_locations.update(new_beam_locations)
        timeline_counts = new_timeline_counts

    return part_1_split_count, sum(timeline_counts.values())



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

    assert day7(test_input) == (21,40)
    with open('inputs/day07.txt') as flines:
        input_str = flines.read()

    print("day 7: ", day7(input_str))

