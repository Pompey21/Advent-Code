"""
Hello, hello! This is the first puzzle of Day 2!
Day 2: https://adventofcode.com/2021/day/2
"""

with open('input.txt') as f:
    lines = f.readlines()

processed = [line[:-1].split() for line in lines]
print(processed)

depth = 0
horizontal = 0
aim = 0

for move in processed:
	if move[0]=='forward':
		horizontal += int(move[1])
		depth += int(move[1])*aim
	elif move[0]=='down':
		# depth += int(move[1])
		aim += int(move[1])
	elif move[0]=='up':
		# depth -= int(move[1])
		aim -= int(move[1])

print(f'Depth: {depth}')
print(f'Horizonntal: {horizontal}')
print(f'Product: {depth*horizontal}')

