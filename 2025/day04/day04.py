# %%
"""
--- Day 4: Printing Department ---
You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
"""
# %%
import numpy as np
FILE = "day04.txt"

class PaperRolls:
    def __init__(self):
        with open(FILE, "r") as f:
            paper_rolls = np.array([[slot=="@" for slot in row] for row in f.read().splitlines()])
            num_rows, num_cols = paper_rolls.shape

            self.paper_rolls = paper_rolls
            self.paper_roll_starting_snapshot = paper_rolls.copy()
            self.num_rows = num_rows
            self.num_cols = num_cols

    def get_section(self, row, col, radius=1):
        row_start = max(row - radius, 0)
        row_end = min(row + radius + 1 , self.num_rows)

        col_start = max(col - radius, 0)
        col_end = min(col + radius + 1, self.num_cols)

        section = self.paper_rolls[row_start:row_end, col_start:col_end]

        return section
    
    def loop_over_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                yield row, col
    
    def is_accessible_roll(self, row, col, max_neighbors=4, radius=1):
        if not self.is_roll(row, col):
            return False
        curr_role = 1
        section = self.get_section(row, col, radius)
        status = section.sum() < max_neighbors + curr_role
        return status
    
    def remove_roll(self, row, col, max_neighbors, radius):
        if self.is_accessible_roll(row, col, max_neighbors, radius):
            self.paper_rolls[row, col] = False
            return 1 # removed
        return 0 # not removed

    def is_roll(self, row, col):
        return self.paper_rolls[row, col]
    
    def count_available_paper_rolls_without_removal(self, max_neighbors=4, radius=1):
        available_rolls = 0
        for row, col in self.loop_over_grid(): 
            if not self.is_roll(row, col):
                continue
            if self.is_accessible_roll(row, col, max_neighbors, radius):
                available_rolls += 1
        return available_rolls
    
    def remove_all_rows(self, max_neighbors=4, radius=1):
        check_again = True
        while check_again:
            changes_this_loop = 0
            for row, col in self.loop_over_grid():
                changes_this_loop += self.remove_roll(row, col, max_neighbors, radius)
            check_again = changes_this_loop > 0

    def num_rolls_removed(self):
        rolls_at_start = self.paper_roll_starting_snapshot.sum()
        rolls_now = self.paper_rolls.sum()
        return rolls_at_start - rolls_now

p = PaperRolls()
answer1 = p.count_available_paper_rolls_without_removal(max_neighbors=4, radius=1)
print(f"Part 1: There are {answer1} accessible rolls")

p.remove_all_rows()
rolls_removed = p.num_rolls_removed()
print(f"Part 2: We removed {rolls_removed} rolls")
# %%
"""
--- Part Two ---
Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
"""