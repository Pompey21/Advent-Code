"""
Hello, hello! This is the puzzle of Day 8!
Day 8: https://adventofcode.com/2021/day/8
"""


# print(inputt)

# num_dict = {'1':0,
# 			'4':0,
# 			'7':0,
# 			'8':0}
# for elem in inputt:
# 	if len(elem) == 2:
# 		num_dict['1'] = num_dict.get('1')+1
# 	elif len(elem) == 4:
# 		num_dict['4'] = num_dict.get('4')+1
# 	elif len(elem) == 3:
# 		num_dict['7'] = num_dict.get('7')+1
# 	elif len(elem) == 7:
# 		num_dict['8'] = num_dict.get('8')+1

# print(num_dict)
# print('TASK 1\n')
# result = sum([num_dict.get(x) for x in num_dict.keys()])
# print(f'result: {result}')
# print()

print('TASK 2\n')
# print(inputt)


def decoder(line_of_input):
	components = {}
	numbers = {}
	for elem in line_of_input:
		if len(elem) == 2:
			numbers[1] = set([char for char in elem])
		elif len(elem) == 3:
			numbers[7] = set([char for char in elem])
		elif len(elem) == 4:
			numbers[4] = set([char for char in elem])
		elif len(elem) == 7:
			numbers[8] = set([char for char in elem])

	for elem in line_of_input:
		if len(elem) == 6 and len(numbers[1] & set([char for char in elem])) == 1:
			numbers[6] = set([char for char in elem])
		elif len(elem) == 5 and len(set([char for char in elem]) & numbers[7]) == 3:
			numbers[3] = set([char for char in elem])

	# print()
	# print(numbers)

	components['a'] = set(numbers[7]) - set(numbers[1])
	components['c'] = set(numbers[8]) - set(numbers[6])
	components['f'] = set(numbers[1]) - components.get('c')
	components['g'] = set(numbers[3]) - (set(numbers[7]) | set(numbers[4]))
	components['d'] = set(numbers[3]) - (set(numbers[7]) | components.get('g'))
	components['b'] = set(numbers[4]) - (set(numbers[7]) | components.get('d'))
	components['e'] = set(numbers[8]) - (set(numbers[4]) | set(numbers[3]))

	# print()
	# print(components)

	# translating the result
	last4 = line_of_input[-4:]
	first = list2number([char for char in last4[0]],components)
	second = list2number([char for char in last4[1]],components)
	third = list2number([char for char in last4[2]],components)
	fourth = list2number([char for char in last4[3]],components)

	return int(str(first)+str(second)+str(third)+str(fourth))

def list2number(lst_chars,components_dict):
	if len(lst_chars) == 7:
		return 8
	elif len(lst_chars) == 2:
		return 1
	elif len(lst_chars) == 3:
		return 7
	elif len(lst_chars) == 4:
		return 4
	elif len(lst_chars) == 6 and len(components_dict.get('e') & set(lst_chars)) == 0:
		return 9
	elif len(lst_chars) == 6 and len(components_dict.get('d') & set(lst_chars)) == 0:
		return 0
	elif len(lst_chars) == 6 and len(components_dict.get('c') & set(lst_chars)) == 0:
		return 6
	elif len(lst_chars) == 5 and len(components_dict.get('c') & set(lst_chars)) == 1 and len(components_dict.get('f') & set(lst_chars)) == 1:
		return 3
	elif len(lst_chars) == 5 and len(components_dict.get('f') & set(lst_chars)) == 0:
		return 2
	else:
		return 5



with open('input.txt') as f:
	# task 1:
	# lines_result = [elem.split('|')[1][:-1].split(' ') for elem in f.readlines()]
	# task 2:
	lines = [elem[:-1].split(' ') for elem in f.readlines()]
	inputt = [decoder(line_of_input) for line_of_input in lines]
	# print(lines)

	result = sum(inputt)
	print(result)
	# result = decoder(inputt)
	# print(result)















