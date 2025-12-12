from collections import deque
from functools import cache

def day11_part_1(input_str: str) -> int:
    """
    receive: a list of device: outputs

    part 1: find every path from device 'you' to device 'out' (which isn't in the list)
    """
    graph = {}  # source -> dests

    for line in input_str.split('\n'):
        if not line.strip():
            continue
        device, device_outputs = line.strip().split(':')
        device_outputs = device_outputs.strip().split(' ')


        graph[device] = device_outputs

    visited = set()
    part_1 = []
    queue = deque((['you'],))
    while queue:
        path = queue.popleft()
        visited.add(tuple(path))

        neighbours = graph[path[-1]]  # fine since 'out' never goes in
        for neighbour in neighbours:
            if neighbour == 'out':
                part_1.append(path + ['out'])
            else:
                if tuple(path + [neighbour]) not in visited:
                    queue.append(path + [neighbour])


    return len(part_1)


def day11_part_2(input_str: str) -> int:
    """
    receive: a list of device: outputs

    part 2: find every path from 'svr' to 'out' that include 'dac' and 'fft'
    """
    graph = {}  # source -> dests

    for line in input_str.split('\n'):
        if not line.strip():
            continue
        device, device_outputs = line.strip().split(':')
        device_outputs = device_outputs.strip().split(' ')


        graph[device] = device_outputs


    # recursive with memoisation. num paths(node) = sum(num_paths(child) for child in children)
    required = {'dac', 'fft'}
    @cache
    def count_paths(node: str, visited_required: frozenset) -> int:
        if node in required:
            visited_required = visited_required | {node}

        if node == 'out':
            # Only count if we've visited all required nodes
            return 1 if visited_required == required else 0

        return sum(
            count_paths(child, visited_required)
            for child in graph.get(node, [])
        )

    return count_paths('svr', frozenset())


if __name__ == "__main__":



    # todays puzzle has different inputs for part 1 and part 2
    test_input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

    test_input_2 = """ svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
    assert day11_part_1(test_input) == 5
    assert day11_part_2(test_input_2) == 2
    with open('inputs/day11.txt') as flines:
        input_str = flines.read()

    print("day 11: ", day11_part_1(input_str))
    print("day 11.2: ", day11_part_2(input_str))


