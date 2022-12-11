import numpy as np
import matplotlib.pyplot as plt


class Day8:
    def __init__(self):
        with open('day08.txt', 'r') as f:
            self.data = np.array([list(map(int, list(line)))
                                 for line in f.read().splitlines()])

    def calc_visible_trees(self):
        x1, y1 = self.scan_xy()
        x2, y2 = self.scan_xy(flip=True)
        visible_trees = x1 | x2 | y1 | y2
        print(f'The number of visible trees is {visible_trees.sum()}')
        plt.imshow(visible_trees, cmap='Greys')
        plt.show()
        self.visible_trees = visible_trees

    def scan_xy(self, flip=False):
        if flip:
            data = total_flip(self.data)
        else:
            data = self.data
        row_size, col_size = data.shape
        row_side = -np.ones(row_size)
        col_side = -np.ones(col_size)
        col_scan = []
        row_scan = []

        for i in range(row_size):
            row = data[i, :]
            row_scan.append(row_side < row)
            row_side = np.maximum(row, row_side)

        for i in range(col_size):
            row = data[:, i]
            col_scan.append(col_side < row)
            col_side = np.maximum(row, col_side)

        col_scan = np.transpose(col_scan)

        if flip:
            return map(total_flip, (row_scan, col_scan))
        else:
            return row_scan, col_scan

    def calc_scenic_score(self):
        data = self.data
        x, y = data.shape
        scenic_scores = np.zeros((x, y), dtype=int)
        for i in range(x):
            for j in range(y):
                curr = data[i, j]
                west = np.flip(data[i, :j])
                east = data[i, j+1:]
                south = data[i+1:, j]
                north = np.flip(data[:i, j])
                directions = (north, south, east, west)
                views = np.array([visibility(curr, view)
                                  for view in directions])
                scenic_score = views.prod()
                scenic_scores[i, j] = scenic_score
        print(f'The best view score is {scenic_scores.max()}')
        plt.imshow(scenic_scores, cmap='hot')
        self.scenic_scores = scenic_scores


def total_flip(data):
    return np.fliplr(np.flipud(data))


def visibility(curr, path):
    num_trees = -1
    for num_trees, tree in enumerate(path):
        if curr <= tree:
            break
    return num_trees + 1


d = Day8()
d.calc_visible_trees()
d.calc_scenic_score()
# %%
