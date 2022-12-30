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
        self.places_gone = []

    def progress_n(self, n):
        for _ in range(n):
            self.progress()

    def progress(self):
        curr_position = self.get_position(self.curr_loc)
        self.inspect_position(curr_position)
        shortest_distance = self.worst_distance
        for p in curr_position.possible_next_positions:
            if p.distance_from_destination < shortest_distance:
                next_loc = p.loc
                shortest_distance = p.distance_from_destination
        self.curr_loc = next_loc

    def get_position(self, loc):
        p = self.master_map[loc[0], loc[1]]
        return p

    def inspect_position(self, p):
        # If first time visit
        if not p.visited:

            self.places_gone.append(p.loc)

            # Mark as visited
            p.visited = True

            # Find possible next moves
            if p.row != 0:
                next_p = self.master_map[p.row - 1, p.col]
                if not next_p.distance_from_destination:
                    next_p.distance_from_destination = self.distance(
                        next_p.loc)
                if next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)

            if p.row != self.max_row:
                next_p = self.master_map[p.row + 1, p.col]
                if not next_p.distance_from_destination:
                    next_p.distance_from_destination = self.distance(
                        next_p.loc)

                if next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)

            if p.col != 0:
                next_p = self.master_map[p.row, p.col - 1]
                if not next_p.distance_from_destination:
                    next_p.distance_from_destination = self.distance(
                        next_p.loc)
                if next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)

            if p.col != self.max_col:
                next_p = self.master_map[p.row, p.col + 1]
                if not next_p.distance_from_destination:
                    next_p.distance_from_destination = self.distance(
                        next_p.loc)
                if next_p.val <= p.val + 1:
                    p.possible_next_positions.append(next_p)

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
        self.visited = False
        self.distance_from_destination = None

    def __repr__(self):
        return f'{self.loc} ({self.distance_from_destination})'


# %%
T = Topography()

T.progress_n(75)

plt.imshow(T.display_map)
plt.scatter(*T.start_loc[::-1], c='red', marker='>')
plt.scatter(*T.destination_loc[::-1], c='green')
d = np.array(T.places_gone)
plt.scatter(d[:, 1], d[:, 0], c='yellow', marker='.', alpha=0.3)
plt.title('Topographical Map')
plt.show()

# %%
d
# %%
