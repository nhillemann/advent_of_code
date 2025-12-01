# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    def part_1(self) -> int:
        """Calculate the number of times the dial points at 0 after any rotation."""
        current_position = 50
        times_at_zero = 0
        
        # self.input contains each line from input.txt as a string
        for rotation in self.input:
            if not rotation.strip():  # Skip empty lines
                continue
                
            direction = rotation[0]
            distance = int(rotation[1:])
            
            # Apply rotation
            if direction == 'L':
                current_position = (current_position - distance) % 100
            else:  # direction == 'R'
                current_position = (current_position + distance) % 100
            
            # Check if pointing at 0 after this rotation
            if current_position == 0:
                times_at_zero += 1
        
        return times_at_zero
        
    def part_2(self) -> int:
        """Part 2 will be solved later."""
        return 0