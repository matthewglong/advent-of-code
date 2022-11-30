# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 binary_grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your binary_grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light binary_grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.


class Day6:
    def __init__(self):
        with open('day06.txt', 'r') as f:
            self.data = f.read().splitlines()
        r = range(1000)
        self.binary_grid = [[False for j in r] for i in r]
        self.volume_grid = [[0 for j in r] for i in r]
        self.run_directions()

    def follow_direction(self, raw_direction):
        d = Direction(raw_direction)
        for row in range(d.row_start, d.row_end + 1):
            for col in range(d.col_start, d.col_end + 1):
                self.binary_grid[row][col] = d.binary_command(
                    self.binary_grid[row][col])
                self.volume_grid[row][col] = d.volume_command(
                    self.volume_grid[row][col])

    def run_directions(self):
        func = self.follow_direction
        for raw_direction in self.data:
            func(raw_direction)

    def answer1(self):
        total = sum([sum(row) for row in self.binary_grid])
        print(f'p1: {total}')
        return total

    def answer2(self):
        total = sum([sum(row) for row in self.volume_grid])
        print(f'p2: {total}')
        return total


class Direction:
    def __init__(self, raw_direction):
        command_translator = {
            'turn on ': (self.binary_turn_on, self.volume_turn_on),
            'turn off ': (self.binary_turn_off, self.volume_turn_off),
            'toggle ': (self.binary_toggle, self.volume_toggle)
        }
        for k, v in command_translator.items():
            if raw_direction.startswith(k):
                self.binary_command, self.volume_command = v
                raw_direction = raw_direction[len(k):]
                break
        first, last = raw_direction.split('through')
        self.row_start, self.col_start = [int(i) for i in first.split(',')]
        self.row_end, self.col_end = [int(i) for i in last.split(',')]

    def binary_turn_on(self, light):
        return True

    def volume_turn_on(self, light):
        return light + 1

    def binary_turn_off(self, light):
        return False

    def volume_turn_off(self, light):
        return max(0, light - 1)

    def binary_toggle(self, light):
        return not light

    def volume_toggle(self, light):
        return light + 2


day = Day6()
day.answer1()
day.answer2()
