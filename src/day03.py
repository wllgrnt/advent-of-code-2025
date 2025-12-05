"""
Input text corresponds to batteries, each labelled with a joltage rating [1-9].
Each line is a battery bank.
You must turn on exactly two batteries. - the joltage is the number formed
(e.g if you turn on 2 and 4, you get 24).
Part 1: Find the largest joltage for each bank

"""

def find_largest_joltage_part1(bank: list[int]) -> int:
    # two-pass. Find the biggest first digit. Then the biggest second digit.
    max_val = -1
    max_i = -1
    for i, val in enumerate(bank[:-1]):
        if val > max_val:
            max_i = i
            max_val = val

    max_val2 = -1
    max_j = -1
    for j, val in enumerate(bank[max_i+1:]):
         if val > max_val2:
            max_j = j
            max_val2 = val

    assert max_j != -1 and max_i != -1

    return max_val*10 + max_val2

def find_largest_joltage_part2(bank: list[int]) -> int:
    # twelve-pass. Find the biggest first digit. Then the biggest second digit. etc
    num_digits = 12
    max_vals = [-1] * num_digits
    max_indices = [-1] * num_digits

    prev_max_index = -1

    for digit_number in range(num_digits):
        for i, val in enumerate(bank[prev_max_index+1: len(bank)-num_digits + digit_number+1], start=prev_max_index+1):
            if val > max_vals[digit_number]:
                max_indices[digit_number] = i
                max_vals[digit_number] = val
        prev_max_index = max_indices[digit_number]

    assert all(i != -1 for i in max_indices)

    final_sum = 0
    for power_of_ten, val in enumerate(max_vals[::-1]):
        final_sum += val * 10 ** power_of_ten

    return final_sum



def day3(input_str) -> tuple[int, int]:
    """Find the largest first digit, then the largest second digit."""
    banks = [[int(char) for char in line] for line in input_str.split('\n') if line]

    return sum(find_largest_joltage_part1(bank) for bank in banks), sum(find_largest_joltage_part2(bank) for bank in banks)



test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

assert day3(test_input) == (357, 3121910778619)

if __name__ == "__main__":

    with open('inputs/day03.txt') as flines:
        input_str = flines.read()

    print("day 3: ", day3(input_str))
