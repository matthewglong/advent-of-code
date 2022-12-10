import re

# Part 1
def is_contained(assignment):
    assignment = list(map(int, re.split('-|,', assignment.strip())))
    if (assignment[0] <= assignment[2] and assignment[1] >= assignment[3]) or \
            (assignment[0] >= assignment[2] and assignment[1] <= assignment[3]):
        return True
    else:
        return False

# Part 2
def overlaps(assignment):
    assignment = list(map(int, re.split('-|,', assignment.strip())))
    print(assignment)
    if (assignment[1] < assignment[2]) or (assignment[3] < assignment[0]):
        return False
    else:
        return True

with open('data.txt', 'r') as f:
    data = map(overlaps, f.readlines())

print(sum(data))
