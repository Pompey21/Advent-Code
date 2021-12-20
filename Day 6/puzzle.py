"""
Hello, hello! This is the puzzle of Day 6!
Day 6: https://adventofcode.com/2021/day/6
"""

# read file
with open('input.txt') as f:
	inputt = [int(elem) for elem in f.readlines()[0].split(',')]

print(inputt)

track = [0,0,0,0,0,0,0,0,0]

for i in range(9):
	count = 0
	for elem in inputt:
		if elem == i:
			count += 1
	track[i] = count

print(track)

days = 256
pointer = 0
for day in range(0,days):
	num_fish = track[pointer]
	track[(pointer+7)%9] = track[(pointer+7)%9] + num_fish
	pointer = (pointer+1) % 9

count_all_fish = sum(track)

print(count_all_fish)


