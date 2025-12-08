# %%
"""
--- Day 5: Cafeteria ---
As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32
The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
"""

FILE = "day05.txt"

def clean_ranges(raw_ranges):
        raw_ranges = sorted(raw_ranges)
        clean_ranges = []
        prev = raw_ranges[0]
        for curr in raw_ranges[1:]:
            if (prev[1] >= curr[0] - 1):
                prev = [prev[0], max(prev[1], curr[1])]
            else:
                clean_ranges.append(prev)
                prev = curr
        if prev != curr:
            clean_ranges.append([prev[0], max(prev[1], curr[1])])
        return clean_ranges

class Inventory:
    def __init__(self, file=FILE):
        with open(file, "r") as f:
            r_fresh, r_available = f.read().split("\n\n")
        raw_ranges = [list(map(int, r.split("-"))) for r in r_fresh.splitlines()]
        clean_raw_ranges = clean_ranges(raw_ranges)
        fresh_ranges = [range(r[0], r[1]+1) for r in clean_raw_ranges]
        available = list(map(int, r_available.splitlines()))
        self.fresh_ranges = fresh_ranges
        self.available = available
        # self.raw_ranges = [list(map(int, r.split("-"))) for r in r_fresh.splitlines()]
    def get_fresh(self):
        fresh_ingredients = list()
        for ingredient in self.available:
            for fresh_range in self.fresh_ranges:
                if ingredient in fresh_range:
                    fresh_ingredients.append(ingredient)
                    break
        return fresh_ingredients
    
    def count_fresh(self):
        fresh_ingredients = self.get_fresh()
        return len(fresh_ingredients)
    
    def get_possible_fresh_DEPRECATED(self):
        possible_fresh = set()
        for fresh_range in self.fresh_ranges:
            new_range = set(fresh_range)
            print(new_range)
            possible_fresh = possible_fresh.union(new_range)
        return possible_fresh
    
    def clean_ranges(self, raw_ranges):
        raw_ranges = sorted(raw_ranges)
        clean_ranges = []
        prev = raw_ranges[0]
        for curr in raw_ranges[1:]:
            if (prev[1] >= curr[0] - 1):
                prev = [prev[0], max(prev[1], curr[1])]
            else:
                clean_ranges.append(prev)
                prev = curr
        if prev != curr:
            clean_ranges.append([prev[0], max(prev[1], curr[1])])
        return clean_ranges
    
    def get_possible_fresh(self):
        total = 0
        for r in self.fresh_ranges:
            total += r.stop - r.start
        return total

        
inventory = Inventory()
fresh_count = inventory.count_fresh()
print(f"Part 1: There are {fresh_count} fresh ingredients")

possible_fresh = inventory.get_possible_fresh()
print(f"Part 2: There are {possible_fresh} possible fresh ingredients")
# %%

"""
--- Part Two ---
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
"""