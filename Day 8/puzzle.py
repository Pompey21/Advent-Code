"""
Hello, hello! This is the puzzle of Day 8!
Day 8: https://adventofcode.com/2021/day/8
"""

with open('test_input.txt') as f:
	# task 1:
	# lines = [elem.split('|')[1][:-1].split(' ') for elem in f.readlines()]
	# task 2:
	lines = [elem[:-1].split(' ') for elem in f.readlines()]
	inputt = [item for sublist in lines for item in sublist if item != '']
print(inputt)

num_dict = {'1':0,
			'4':0,
			'7':0,
			'8':0}
for elem in inputt:
	if len(elem) == 2:
		num_dict['1'] = num_dict.get('1')+1
	elif len(elem) == 4:
		num_dict['4'] = num_dict.get('4')+1
	elif len(elem) == 3:
		num_dict['7'] = num_dict.get('7')+1
	elif len(elem) == 7:
		num_dict['8'] = num_dict.get('8')+1

print(num_dict)
print('TASK 1\n')
result = sum([num_dict.get(x) for x in num_dict.keys()])
print(f'result: {result}')
print()

print('TASK 2\n')
print(inputt)