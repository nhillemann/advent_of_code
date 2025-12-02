# Day 1 (2025)

`TITLE` ([prompt](https://adventofcode.com/2025/day/1))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

The Problem:

- Dial with arrow
- Around dial: numbers 0 - 99
- Input: Sequence of rotations
- One per line
- 1 Rotation starts with either L (left) or R (right) direction
- After direction: distance value (how many numbers is it moving in this direction)
- Circle movement: 0 - 99, than 0 again and so on...
- Starting point before first rotation: 50

The password is the number of times the dial is left pointing at 0 after any rotation in the sequence!

The Solution:

- Variable for starting point (starts with == 50)
- Variable for the sign (movement direction): L == - and R == + based on parsed input.txt
- Variable for the distance value based on parsed input.txt
- Variable for number of current position after 1 rotation
- Variable for absolute numbers of "number of current position after 1 rotation" == 0
- Loop creates 1 rotation:
    - Read starting point variable
    - Read the sign and the distance value next
    - Calculate starting point sign (+ or -) with distance value
    - Safe result in Variable for the number of current position after 1 rotation
    - If result == 0 --> ++ Variable for absolute numbers of "number of current positions after 1 rotation" == 0
    - move on to the next line of parsed input and update Variable for the sign and distance value.
- If all rotations are done: Read Variable for absolute numbers of "number of current position after 1 rotation" == 0

## Part 2

The Problem:

- The problem in Part 1 will be changed to one aspect
- The password now is the number of times the dial is left pointing at 0 during AND after any rotation in the sequence
- When moving large distances, the dial can pass through 0 multiple times

The Solution:

- Variables will be used mostly like in Part 1
- Exceptions are:
- Variable for starting point (starts with == 50) will be changed in 
- Variable for current position (starts with == 50)
- Variable for absolute numbers of "current positions after 1 rotation" == 0 will be changed in
- Variable for total zeros (counts all times dial points at 0)

- Loop creates 1 rotation:
    - Read current position variable
    - Read the sign and the distance value next
    - Calculate how many time dial passes through 0 during rotation
        - If direction == R (right/forward):
            - Start counting from current position + 1
            - End at current position + distance
            - Number of zeros = (end // 100) - ((start - 1) // 100)
        - If direction == L (left/backward):
            - Start counting from current position - 1
            - End at current_position - distance
            - Handle wrap-around: if end < 0, wrapp past 0
            - Calculate zeros separately before and after wrap 
    - Safe result of zero count after 1 rotation to total zeros
    - Update current position to final position (current position sign distance) % 100
    - move on to the next line of parsed input and update Variable for the sign and distance value.
- If all rotations are done: Read Variable for total zero
