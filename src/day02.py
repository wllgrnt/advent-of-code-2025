"""
"""

import math

def is_invalid_part2(product_id: int) -> bool:
    """Return True if product_id has only repeating digits.

    Get the number of digits.
    if 1,2,3,4...// num_digits/2 fit cleanly, then if

    split into 1s. split into 2s. split into threes, etc.
    """
    if product_id < 10:
        return False
    product_id = str(product_id)
    for split_size in range(1, len(product_id) // 2 + 1):
        if len(product_id) % split_size != 0:
            continue
        if len(set(product_id[i*split_size:(i+1)*split_size] for i in range(len(product_id) // split_size))) == 1:
            return True

    return False

def is_invalid_part1(product_id: int) -> bool:
    """Return True if product_id splits cleanly into 2 and the two parts match."""
    num_digits = int(math.log10(product_id)) + 1
    split_value = 10**(num_digits // 2)
    return product_id // split_value == product_id % split_value



def day2(product_ranges: str) -> tuple[int, int]:
    """parse the comma-separated list of ranges.
    find any value in range [start, end] that's has any repeated sequence (call these invalid).

    return the sum of invalid ids.

    start the slow way.

    """
    invalid_sum_part1, invalid_sum_part2 = 0, 0
    for product_range in product_ranges.split(','):
        start, end = product_range.split('-')
        for val in range(int(start), int(end) + 1):
            if is_invalid_part1(val):
                invalid_sum_part1 += val
            if is_invalid_part2(val):
                invalid_sum_part2 += val

    return invalid_sum_part1, invalid_sum_part2





test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"""

assert day2(test_input) == (1227775554, 4174379265)

if __name__ == "__main__":

    with open('inputs/day02.txt') as flines:
        input_str = flines.read()

    print("day 2: ", day2(input_str))
