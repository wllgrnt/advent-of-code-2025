import numpy as np
from functools import reduce
from operator import add, mul
def day6(input_str: str):
    """input: a list of columns of numbers, with the final row being the operation to perform (either + or *).
    
    returns: the sum of the reduction operation.

    part two addendum: read numbers right-to-left, top-to-bottom. 
    eg
    64
    23
    314
    +

    means 4 + 431 + 623
    """
    input_list = ((int(x) for x in line.split()) for line in input_str.split("\n")[:-1] if line.strip())

    operations = input_str.split("\n")[-1].split()
    
    running_sum = 0
    for col, op in zip(zip(*input_list), operations):
        match op:
            case '*':
                running_sum += reduce(mul, col)
            case '+':
                running_sum += reduce(add, col)
            case _:
                raise ValueError()
           
    input_arr = np.asarray([[x for x in line] for line in input_str.split('\n')])

    # traverse through the input_arr backwards, building the numbers.
    number_stack = []
    part_two = 0
    for col_idx in range(input_arr.shape[1]-1, -1, -1):
        
        col = input_arr[:, col_idx]
        int_str = ''.join(col[:-1])
        if not int_str.split():
            continue
        number_stack.append(int(int_str))
        if op := col[-1].strip():
            # blow the stack
            match op:
                case '*':
                    part_two += reduce(mul, number_stack)
                case '+':
                    part_two += reduce(add, number_stack)
                case _:
                    raise ValueError()
            number_stack = []
    
    # print(part_two)
    return running_sum, part_two


if __name__ == "__main__":

    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    assert day6(test_input) == (4277556,3263827)
    with open('inputs/day06.txt') as flines:
        input_str = flines.read()

    print("day 6: ", day6(input_str))

