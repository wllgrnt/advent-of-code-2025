"""
Parse a list of rotations as a string on a safe dial which starts at position 50 and has values 0-99.
part 1: count every time you hit 0
part 2: count every time you move through 0
"""


def day1(rotation_list: str) -> tuple[int, int]:
    """dial is numbers 0 to 99 in order. Run the rotations in input_str and count the number of 0s,
    and the number of times through 0"""
    current_position = 50
    dial_size = 100
    zero_count_part1 = 0
    zero_count_part2 = 0
    for line in rotation_list.split("\n"):
        if line:
            direction = line[0]
            magnitude = int(line[1:])
            if direction not in ('L', 'R'):
                raise ValueError(f'unexpected direction {direction}')
            int_dir = 1 if direction == 'R' else -1
            delta = int_dir * magnitude
            move = current_position + delta

            if delta > 0:
                zero_visits = move // 100 - current_position // 100
            elif delta < 0:
                zero_visits = (current_position - 1 ) // 100 - (move -1 ) // 100
            else:
                zero_visits = 0

            zero_count_part2 += zero_visits
            current_position =  move % dial_size
            if current_position == 0:
                zero_count_part1 += 1

    return zero_count_part1, zero_count_part2


test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

assert day1(test_input) == (3, 6)


if __name__ == "__main__":

    with open('inputs/day01.txt') as flines:
        input_str = flines.read()

    print("part 1: ", day1(input_str))
