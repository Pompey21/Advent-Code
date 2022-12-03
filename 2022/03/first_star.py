import string
from collections import defaultdict

with open("input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line[:-1])

print(lines)

# halving the contents based on compartments!
backpacks = [(backpack[:len(backpack)//2],backpack[len(backpack)//2:]) for backpack in lines]

print(backpacks)

counter = defaultdict(int)
num_occurences = defaultdict(int)
for comp_1,comp_2 in backpacks:
    comp_1 = set(comp_1)
    comp_2 = set(comp_2)
    interstection = comp_1.intersection(comp_2)
    # print(interstection)
    for char in interstection:
        num_occurences[char] += 1

# print(num_occurences)

# counting priorities
alphabet_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority_score = list(range(1,53))

priority_score_dict = dict(zip(alphabet_list, priority_score))

score = 0
for char in num_occurences.keys():
    times = num_occurences[char]
    score += times * priority_score_dict[char]

print(score)


