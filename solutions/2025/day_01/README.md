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
- Variable for absolute numbers of "number of current positions" == 0
- Loop creates 1 rotation:
    - Read starting point variable
    - Read the sign and the distance value next
    - Calculate starting point sign (+ or -) with distance value
    - Safe result in Variable for the number of current position after rotation
    - If result == 0 --> ++ Variable for absolute numbers of "number of current positions" == 0
    - move on to the next line of parsed input and update Variable for the sign and distance value.
- If all rotations are done: Read Variable for absolute numbers of "number of current positions" == 0

## Part 2

Will be solved later!