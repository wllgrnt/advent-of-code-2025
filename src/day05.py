from dataclasses import dataclass
import numpy as np
@dataclass
class FreshRange:
    start: int 
    end: int

    def overlaps(self, other):
        return max(self.start, other.start) <= min(self.end, other.end)

    def __lt__(self, other):
        return self.start < other.start   
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, FreshRange) and self.start == other.start and self.end == other.end

def day5(input_str: str):
    """
    Take a list of fresh ingredient ID ranges, a blank line, and available IDS.
    Return the number of fresh, available ingredient IDs.    
    """
    ranges_str, available_str = input_str.split("\n\n")
    ranges = []
    for range in ranges_str.split("\n"):
        start, end = range.split("-")
        ranges.append(FreshRange(start=int(start), end=int(end)))
    available = [int(x) for x in available_str.split('\n') if x.strip()]

    # part one - intersection of available and fresh
    fresh_and_available = 0
    for ingredient in available:
        for range in ranges:
            if range.start <= ingredient <= range.end:
                fresh_and_available += 1
                break 
    
    # part two - all fresh. Merge the ranges where they overlap.
    merged_ranges = []
    for range in sorted(ranges):
        for prev_range in merged_ranges:
            if prev_range.overlaps(range):
                prev_range.start = min(prev_range.start, range.start)
                prev_range.end = max(prev_range.end, range.end)
                break
        else:
            merged_ranges.append(range)



    all_fresh = sum(x.end - x.start + 1 for x in merged_ranges)
    return fresh_and_available, all_fresh


if __name__ == "__main__":

    test_input = """3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32"""

    assert day5(test_input) == (3, 14)
    with open('inputs/day05.txt') as flines:
        input_str = flines.read()

    print("day 5: ", day5(input_str))

