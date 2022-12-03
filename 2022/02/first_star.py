
with open("input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line[:-1])

first_player_hand = {
    "A" : 'rock',
    'B' : 'paper',
    'C' : 'scissors'
}

second_player_hand = {
    'X' : 'rock',
    'Y' : 'paper',
    'Z' : 'scissors'
}

lines = [(first_player_hand[pair.split(' ')[0]],second_player_hand[pair.split(' ')[1]]) for pair in lines]
print(lines)


hand_score = {
    "rock" : 1,
    "paper" : 2,
    "scissors" : 3
}



def rock_paper_sccissors(player_1,player_2):
    if player_2 == "rock":
        if player_1 == "paper":
            return hand_score[player_2]+0
        elif player_1 == "rock":
            return hand_score[player_2]+3
        else:
            return hand_score[player_2]+6

    elif player_2 == "paper":
        if player_1 == "paper":
            return hand_score[player_2]+3
        elif player_1 == "rock":
            return hand_score[player_2]+6
        else:
            return hand_score[player_2]+0

    else:
        if player_1 == "paper":
            return hand_score[player_2]+6
        elif player_1 == "rock":
            return hand_score[player_2]+0
        else:
            return hand_score[player_2]+3

total_score = 0

for player_1,player_2 in lines:
    total_score += rock_paper_sccissors(player_1,player_2)

print(total_score)

# tests
print(rock_paper_sccissors("rock","paper"))
print(rock_paper_sccissors("rock","rock"))
print(rock_paper_sccissors("rock","scissors"))
print(rock_paper_sccissors("paper","rock"))
print(rock_paper_sccissors("paper","paper"))
print(rock_paper_sccissors("paper","scissors"))
print()
print(rock_paper_sccissors("scissors","rock"))
print(rock_paper_sccissors("scissors","paper"))
print(rock_paper_sccissors("scissors","scissors"))



