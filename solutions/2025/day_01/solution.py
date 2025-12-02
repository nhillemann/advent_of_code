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
        """Calculate password using method 0x434C49434B (CLICK)."""
        current_position = 50
        total_zeros = 0
        
        for rotation in self.input:
            if not rotation.strip():
                continue
                
            direction = rotation[0]
            distance = int(rotation[1:])
            
            # For both directions, count zeros by checking every position through pass
            
            if direction == 'R':
                # Check each position
                for step in range(1, distance + 1):
                    pos = (current_position + step) % 100
                    if pos == 0:
                        total_zeros += 1
                
                # Update final position
                current_position = (current_position + distance) % 100
                
            else:  # 'L'
                for step in range(1, distance + 1):
                    pos = (current_position - step) % 100
                    if pos == 0:
                        total_zeros += 1
                
                current_position = (current_position - distance) % 100
        
        return total_zeros