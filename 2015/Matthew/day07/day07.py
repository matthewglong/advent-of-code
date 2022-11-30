import re

pattern = re.compile(r'^([^A-Z]*)\s?([A-Z]*)\s?([^A-Z]*) -> (.+)$')


class Day7:
    def __init__(self):
        with open('day07.txt', 'r') as f:
            self.data = f.read().splitlines()
            self.commands = []
            for d in self.data[:25]:
                self.commands.append(Node(d))


class Node:
    def __init__(self, raw_direction):
        extract = pattern.match(raw_direction)
        self.x, self.operator, self.y, self.r = extract.groups()


tests = [
    'NOT dq -> dr',
    'kg OR kf -> kh',
    '44430 -> b',
    'y AND ae -> ag',
    'lf RSHIFT 2 -> lg',
    '1 AND fi -> fj',
    '2 AND 5 -> fj'
]

d = Day7()
for p in d.commands:
    print(f"x: {p.x}, y: {p.y}")
