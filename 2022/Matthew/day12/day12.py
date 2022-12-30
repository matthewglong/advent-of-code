import numpy as np
import matplotlib.pyplot as plt


class Topography():
    def __init__(self):

        map_dict = {k: v for v, k in enumerate('abcdefghijklmnopqrstuvwxyz')}

        raw_data = []
        with open('day12.txt', 'r') as f:
            for row, l in enumerate(f.read().splitlines()):
                line = []
                for column, square in enumerate(l):
                    if square == 'S':
                        line.append(0)
                        self.start = self.curr_position = [row, column]
                    elif square == 'E':
                        line.append(25)
                        self.destination = [row, column]
                    else:
                        line.append(map_dict[square])
                raw_data.append(line)
        self.master_map = np.array(raw_data)
        self.max_row, self.max_col = self.master_map.shape

    def position_val(self, position):
        row, column = position
        val = self.master_map[row, column]
        return val

    def possible_moves(self, position):
        row, col = position
        move = {}

        curr_val = self.position_val(position)
        print('curr val is', curr_val)

        if row != 0:
            m = [row - 1, col]
            n = self.position_val(m)
            if n <= curr_val + 1:
                move['up'] = m

        if row != self.max_row:
            m = [row + 1, col]
            n = self.position_val(m)
            if n <= curr_val + 1:
                move['down'] = m

        if col != 0:
            m = [row, col - 1]
            n = self.position_val(m)
            if n <= curr_val + 1:
                move['left'] = m

        if col != self.max_col:
            m = [row, col + 1]
            n = self.position_val(m)
            if n <= curr_val + 1:
                move['right'] = m

        return move


T = Topography()

print(T.possible_moves([25, 3]))

plt.imshow(T.master_map)
plt.scatter(*T.start[::-1], c='red', marker='>')
plt.scatter(*T.destination[::-1], c='green')
plt.scatter(*[25, 3][::-1], c='yellow', marker='.', alpha=0.3)
plt.title('Topographical Map')
plt.show()
