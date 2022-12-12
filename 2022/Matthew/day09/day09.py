# %%
class Board:
    def __init__(self):
        with open('day09.txt', 'r') as f:
            self.commands = [Command(row) for row in f]
        self.positions = {}
        p = self.access_position(0, 0)
        p.tail_visit = True
        self.head = Token(p)
        self.tail = Token(p)
        self.direction_map = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0)
        }

    def num_tail_visits(self):
        self.simulate()
        num = sum([p.tail_visit for p in self.positions.values()])
        print(f'The number of tail visits is {num}')

    def simulate(self):
        for command in self.commands:
            self.follow_direction(command)

    def follow_direction(self, command):
        new_hx = self.head.position.x
        new_hy = self.head.position.y
        d = command.direction
        x_inc, y_inc = self.direction_map[d]
        for _ in range(command.spaces):
            new_hx += x_inc
            new_hy += y_inc
            p = self.access_position(new_hx, new_hy)
            self.head.position = p
            self.move_tail()

    def access_position(self, x, y):
        k = f"{x}_{y}"
        if k not in self.positions.keys():
            self.positions[k] = Position(x, y)
        return self.positions[k]

    def move_tail(self):
        hx = self.head.position.x
        hy = self.head.position.y
        tx = new_tx = self.tail.position.x
        ty = new_ty = self.tail.position.y

        x_dist = abs(hx - tx)
        y_dist = abs(hy - ty)

        if x_dist > 1:
            new_tx = HF.step_closer(hx, tx)
            if y_dist > 0:
                new_ty = HF.step_closer(hy, ty)

        if y_dist > 1:
            new_ty = HF.step_closer(hy, ty)
            if x_dist > 0:
                new_tx = HF.step_closer(hx, tx)

        p = self.access_position(new_tx, new_ty)
        p.tail_visit = True
        self.tail.position = p


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tail_visit = False

    def __repr__(self):
        return f"x: {self.x}, y: {self.y} [{self.tail_visit}]"


class Token:
    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return f'token --> {self.position}'


class HF:
    def step_closer(leader, follower):
        if leader >= follower:
            return follower + 1
        else:
            return follower - 1


class Command:
    def __init__(self, row):
        self.direction, spaces = row.split()
        self.spaces = int(spaces)

    def __repr__(self):
        return f'{self.direction} for {self.spaces} spaces'


b = Board()
b.num_tail_visits()
