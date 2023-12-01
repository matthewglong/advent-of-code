# %%
import numpy as np
import matplotlib.pyplot as plt


class Topography():
    def __init__(self):

        map_dict = {k: v for v, k in enumerate('abcdefghijklmnopqrstuvwxyz')}

        raw_data = []
        raw_display = []
        with open('day12.txt', 'r') as f:
            for row, l in enumerate(f.read().splitlines()):
                line = []
                for col, square in enumerate(l):
                    if square == 'S':
                        val = 0
                        self.start_loc = self.curr_loc = [row, col]
                    elif square == 'E':
                        val = 25
                        self.destination_loc = [row, col]
                    else:
                        val = map_dict[square]
                    p = Position(row, col, val)
                    line.append(p)
                    raw_display.append(val)
                raw_data.append(line)
        self.master_map = np.array(raw_data)
        s = self.master_map.shape
        self.display_map = np.array(raw_display).reshape(s)
        self.max_row, self.max_col = s
        self.worst_distance = self.max_col + self.max_row
        self.path = []

    def progress_n(self, n):
        for _ in range(n):
            self.progress()

    def progress(self):
        curr_position = self.get_position(self.curr_loc)
        self.inspect_position(curr_position)
        shortest_distance = self.worst_distance
        remaining_next = []
        next_loc = None
        for p in curr_position.possible_next_positions:
            if p.visited:
                pass
            elif p.distance_from_destination < shortest_distance:
                next_loc = p.loc
                shortest_distance = p.distance_from_destination
                remaining_next.append(p)
        curr_position.possible_next_positions = remaining_next
        if next_loc:
            self.curr_loc = next_loc
        else:
            self.path.pop()
            self.curr_loc = self.path[-1]

    def get_position(self, loc):
        p = self.master_map[loc[0], loc[1]]
        return p

    def get_curr_position(self):
        p = self.get_position(self.curr_loc)
        return p

    def inspect_position(self, p):

        p.update_shortest_path(self)

        # If first time visit
        if not p.visited:

            self.path.append(p.loc)

            # Mark as visited
            p.visited = True

            # Find possible next moves
            if p.row != 0:
                next_p = self.master_map[p.row - 1, p.col]
                if p.val <= next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)
                    next_p.set_destination_distance(self.destination_loc)

            if p.row != self.max_row:
                next_p = self.master_map[p.row + 1, p.col]
                
                if p.val <= next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)
                    next_p.set_destination_distance(self.destination_loc)

            if p.col != 0:
                next_p = self.master_map[p.row, p.col - 1]
                
                if p.val <= next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)
                    next_p.set_destination_distance(self.destination_loc)

            if p.col != self.max_col:
                next_p = self.master_map[p.row, p.col + 1]
                
                if p.val <= next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)
                    next_p.set_destination_distance(self.destination_loc)

        # If not our first rodeo
        else:
            pass

    def distance(self, start=None, stop=None):
        if not start:
            start = self.curr_loc
        if not stop:
            stop = self.destination_loc
        manhatt_dist = abs(stop[0]-start[0]) + abs(stop[1]-start[1])
        return manhatt_dist


class Position:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
        self.loc = [row, col]
        self.possible_next_positions = []
        self.shortest_path = []
        self.visited = False
        self.distance_from_destination = None

    def __repr__(self):
        return f'{self.loc} ({self.distance_from_destination})'

    def calc_distance(self, target):
        t_row, t_col = target
        manhatt_dist = abs(t_row-self.row) + abs(t_col-self.col)
        return manhatt_dist

    def set_destination_distance(self, destination):
        if not self.distance_from_destination:
            self.distance_from_destination = self.calc_distance(destination)

    def update_shortest_path(self, T):
        if (not self.shortest_path) or (len(self.shortest_path) > len(T.path)):
            self.shortest_path = T.path.copy()
        else:
            T.path = self.shortest_path




# %%
T = Topography()
T.progress_n(160)
plt.imshow(T.display_map)
plt.scatter(*T.start_loc[::-1], c='red', marker='>')
plt.scatter(*T.destination_loc[::-1], c='green')
d = np.array(T.path)
plt.scatter(d[:, 1], d[:, 0], c='yellow', marker='.', alpha=0.3)
plt.scatter(*d[-1][::-1], c='white', marker='.')
plt.title('Topographical Map')
plt.show()