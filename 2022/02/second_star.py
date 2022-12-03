
with open("input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line[:-1])

first_player_hand = {
    "A" : 'rock',
    'B' : 'paper',
    'C' : 'scissors'
}

result = {
    'X' : 'lose',
    'Y' : 'draw',
    'Z' : 'win'
}

lines = [(first_player_hand[pair.split(' ')[0]],result[pair.split(' ')[1]]) for pair in lines]
print(lines)

scores_convert = {
    'rock' : 1,
    'paper' : 2,
    'scissors' : 3
}

def find_missing_hand(first_player,res):
    if first_player == 'rock':
        if res == 'lose':
            return scores_convert['scissors'] + 0
        elif res == 'draw':
            return scores_convert['rock'] + 3
        elif res == 'win':
            return scores_convert['paper'] + 6

    elif first_player == 'paper':
        if res == 'lose':
            return scores_convert['rock'] + 0
        elif res == 'draw':
            return scores_convert['paper'] + 3
        elif res == 'win':
            return scores_convert['scissors'] + 6

    elif first_player == 'scissors':
        if res == 'lose':
            return scores_convert['paper'] + 0
        elif res == 'draw':
            return scores_convert['scissors'] + 3
        elif res == 'win':
            return scores_convert['rock'] + 6

total_score = 0
for player_1,player_2 in lines:
    total_score += find_missing_hand(player_1,player_2)

print(total_score)