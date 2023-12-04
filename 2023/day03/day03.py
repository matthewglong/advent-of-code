# %%
"""
--- Day 3: Gear Ratios ---

-- PART ONE --

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to
the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't
expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it."
You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out
which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out
which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots
of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even
diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:
__________
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
__________

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right)
and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the
engine schematic?
"""

# SIMPLE Part 1

# import numpy as np

# with open('day03.txt', 'r') as f:
#     lines = np.array([[char if char in '.0123456789' else ' ' for char in line]
#                      for line in f.read().splitlines()])

# x_size, y_size = lines.shape


# def get_slice(x, y):
#     top_left = max(x-1, 0)
#     top_right = min(x+2, x_size)
#     bottom_left = max(y-1, 0)
#     bottom_right = min(y+2, y_size)
#     slice = lines[top_left:top_right, bottom_left:bottom_right]
#     return slice


# part_numbers = []

# for x in range(x_size):
#     curr_number = ''
#     is_part = False
#     for y in range(y_size):
#         curr_char = lines[x, y]
#         if curr_char > '.':
#             curr_number += curr_char
#             slice = get_slice(x, y)
#             if (slice == ' ').any():
#                 is_part = True
#         else:
#             if bool(curr_number) & is_part:
#                 part_numbers.append(int(curr_number))
#             curr_number = ''
#             is_part = False
#     if bool(curr_number) & is_part:
#         part_numbers.append(int(curr_number))

# print(f"The sum of all of the part numbers is {sum(part_numbers)}.")

"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life,
you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the
gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands
the engineer, holding a phone in one hand and waving with the other. You're going so slowly that
you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any *
symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying
those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer
can figure out which gear needs to be replaced.

Consider the same engine schematic again:

__________
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
__________

In this schematic, there are two gears. The first is in the top left; it has part numbers
467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio
is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.)
Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""


# PREP




import numpy as np
class EngineUnit:
    def __init__(self, char):
        self.char = char
        self.is_number = char in '0123456789'
        self.is_blank = char == '.'
        self.is_symbol = not (self.is_number | self.is_blank)
        self.is_gear = char == '*'
        self.number = None

    def __repr__(self):
        return self.char


class IdentifiedNumber:
    def __init__(self):
        self.working_str_number = ''
        self.number = None
        self.is_part = False
        self.has_data = False

    def __repr__(self):
        if self.number:
            return f"COMPLETE {self.number} (part: {self.is_part})"
        else:
            return f"INCOMPLETE {self.working_str_number}"

    def add_char(self, char):
        self.working_str_number += char
        self.has_data = True

    def submit(self):
        if self.has_data:
            self.number = int(self.working_str_number)
            self.working_str_number = None

    def confirm_part(self):
        self.is_part = True

    def is_real_number(self):
        return self.number >= 0


with open('day03.txt', 'r') as f:
    lines = np.array([[EngineUnit(char) for char in line]
                      for line in f.read().splitlines()])

x_size, y_size = lines.shape


def get_slice(x, y):
    top_left = max(x-1, 0)
    top_right = min(x+2, x_size)
    bottom_left = max(y-1, 0)
    bottom_right = min(y+2, y_size)
    slice = lines[top_left:top_right, bottom_left:bottom_right]
    return slice


check_symbol = np.vectorize(lambda x: x.is_symbol)
check_part = np.vectorize(lambda x: x.number)

# PART ONE
numbers = []
gear_locs = []

for x in range(x_size):
    working_number = IdentifiedNumber()
    for y in range(y_size):
        unit = lines[x, y]
        if unit.is_number:
            unit.number = working_number
            working_number.add_char(unit.char)
            slice = get_slice(x, y)
            if check_symbol(slice).any():
                working_number.confirm_part()
        else:
            if working_number.has_data:
                working_number.submit()
                numbers.append(working_number)
            working_number = IdentifiedNumber()
            if unit.is_gear:
                gear_locs.append((x, y))
    if working_number.has_data:
        working_number.submit()
        numbers.append(working_number)

part_numbers = [num.number for num in numbers if num.is_part]
print(f"The sum of all of the part numbers is {sum(part_numbers)}.")

# PART TWO
gear_ratios = []

for gear_loc in gear_locs:
    slice = get_slice(*gear_loc)
    parts = {part for part in check_part(slice).reshape(-1) if part}
    if len(parts) == 2:
        gear_ratio = 1
        for part in parts:
            gear_ratio *= part.number
        gear_ratios.append(gear_ratio)

print(f"The sum of all of all gear ratios is {sum(gear_ratios)}.")
