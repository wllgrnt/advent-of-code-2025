from dataclasses import dataclass
from collections import deque
from numpy.typing import NDArray
import numpy as np

@dataclass
class Machine:  # make numpys
    desired_config: NDArray[np.bool_]
    button_schematics: list[NDArray[np.bool_]]
    joltage_reqs: set[int]

    @classmethod
    def from_str(cls, input_line):
        print('parsing ', input_line)
        machine_split = input_line.index(']') + 1
        joltage_split = input_line.index('{')
        desired_light_settings = input_line[1: machine_split-1]
        button_schematics = input_line[machine_split: joltage_split]
        joltage_reqs = input_line[joltage_split:]

        # warning: gross parsing below
        desired_light_settings = np.array([char == '#' for char in desired_light_settings], dtype=bool)
        button_schematic_list = []

        for button in button_schematics.strip().split(' '):
            button_arr =np.zeros(len(desired_light_settings), dtype=bool)
            for toggle_loc in button[1:-1].split(','):
                button_arr[int(toggle_loc)] = True
            button_schematic_list.append(button_arr)
        joltage_reqs = eval(joltage_reqs)

        return Machine(desired_light_settings, button_schematic_list, joltage_reqs)


    def get_min_presses(self):
        """ the aim is to match the indicator lights to the diagram. All lights start off.
            you can press the buttons (in the schematics). Each () lists which lights it toggles.
            Determine the fewest total presses required to configure all lights.
        """
        initial_config = np.zeros(len(self.desired_config), dtype=bool)

        # bfs
        # track the number of button presses on the path.
        queue = deque([(initial_config, 0),])

        # track visited states to avoid cycles.
        visited = set()
        while queue:
            current_light_state, num_presses = queue.popleft()
            visited.add(current_light_state.tobytes())

            if np.all(current_light_state == self.desired_config):
                return num_presses

            for button in self.button_schematics:
                new_state = current_light_state ^ button
                if new_state.tobytes() not in visited:
                    queue.append((new_state, num_presses + 1))

        return -1

def day10(input_str: str) -> tuple[int, int]:
    """
    <input_str> has one machine per line. each line has an indicator light diagram in [],
    one or more wiring schematics in (), and joltage reqs in {}
    """
    part1_sum = sum(Machine.from_str(line).get_min_presses() for line in input_str.split('\n') if line.strip())

    return part1_sum,0




if __name__ == "__main__":

    test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

    assert day10(test_input) == (7,0)
    with open('input/day10.txt') as flines:
        input_str = flines.read()

    print("day 10: ", day10(input_str))


