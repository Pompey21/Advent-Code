
with open("input.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line[:-1])

elfs = []
backpack = []
for package in lines:
    if package:
        backpack.append(int(package))
    else:
        elfs.append(sum(backpack))
        backpack = []


big_boi = max(elfs)
print(big_boi)

elfs.sort()

top_three_bois = sum(elfs[::-1][:3])
print(top_three_bois)
