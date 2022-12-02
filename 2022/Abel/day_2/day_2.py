# read in data and convert letters to nummbers
# output list of tuples representing games
with open('data.txt') as f:
    data = []
    conversion = {'A': 0,
                  'B': 1,
                  'C': 2,
                  'X': 0,
                  'Y': 1,
                  'Z': 2}
    for line in f:
        line = line.rstrip().split(' ')
        game = (conversion[line[0]], conversion[line[1]])
        data.append(game)


# PART 1
# determine the score of a given game
def calculate_score(game):
    score = game[1] + 1
    # win
    if (game[0] + 1) % 3 == game[1]:
        score += 6
    # tie
    elif game[0] == game[1]:
        score += 3
    # loss
    else:
        pass
    return score

# iterate over all games
total_score = 0
for game in data:
    total_score += calculate_score(game)

print(total_score)


# PART 2
def calculate_outcome(game):
    opponent = game[0]
    score = 0
    # win
    if game[1] == 2:
        score += 6
        me = (opponent + 1) % 3
        score += me + 1
    # tie
    elif game[1] == 1:
        score += 3
        score += opponent + 1
    # lose
    else:
        me = (opponent + 2) % 3
        score += me + 1
    return score

# iterate over all games
total_score = 0
for game in data:
    total_score += calculate_outcome(game)

print(total_score)
