import string
from collections import defaultdict

with open("input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line[:-1])

trios = []
trio = set(lines[0])
for index,elf in enumerate(lines):
    trio = trio.intersection(set(elf))
    if index%3==2:
        trios.append(list(trio)[0])
        if index+1<len(lines):
            trio = set(lines[index+1])
print(trios)


# counting priorities
alphabet_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority_score = list(range(1,53))

priority_score_dict = dict(zip(alphabet_list, priority_score))

score = 0
for trio in trios:
    score += priority_score_dict[trio]

print(score)