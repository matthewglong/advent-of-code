# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

class Day3:
    def __init__(self, num_santas=1):
        with open('day03.txt', 'r') as f:
            self.data = f.read()
        self.santa_index = 0
        self.max_idx = num_santas - 1
        self.santas = [Santa(name=i) for i in range(num_santas)]
        self.houses = None
        self.count_houses()

    def get_santa(self):
        idx = self.santa_index
        if idx == self.max_idx:
            self.santa_index = 0
        else:
            self.santa_index += 1
        return self.santas[idx]

    def next_house(self, santa, direction):
        if direction == '<':
            santa.x -= 1
        elif direction == '>':
            santa.x += 1
        elif direction == '^':
            santa.y += 1
        elif direction == 'v':
            santa.y -= 1
        else:
            raise ValueError(f'Direction "{direction}" not recognized')
        self.houses.append((santa.x, santa.y))

    def run_delivery(self):
        self.houses = [(santa.x, santa.y) for santa in self.santas]
        for direction in self.data:
            self.next_house(self.get_santa(), direction)

    def count_houses(self):
        if not self.houses:
            self.run_delivery()
        unique_houses = len(set(self.houses))
        print(f"{self.max_idx+1} Santas: {unique_houses} houses")
        return unique_houses


class Santa:
    def __init__(self, name='unnamed'):
        self.name = name
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f"santa-{self.name}@{self.x}|{self.y}"


p1 = Day3()
p2 = Day3(num_santas=2)
p2 = Day3(num_santas=100)
