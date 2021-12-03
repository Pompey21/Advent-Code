"""
Hello, hello! This is the first puzzle of Day 3!
Day 3: https://adventofcode.com/2021/day/3
"""

with open('input.txt') as f:
	lines = f.readlines()

processed = [(line[:-1]) for line in lines]
# print(processed)


# Power Consumption

gamma = ''
epsilon = ''

for digit in range(len(lines[0])-1):
	count_0=0
	count_1=0
	for elem in lines:
		if elem[digit]=='0':
			count_0 += 1
		elif elem[digit]=='1':
			count_1 += 1
	if count_1>count_0:
		gamma += '1'
		epsilon += '0'
	else:
		gamma+='0'
		epsilon+='1'
	print('-------------------')
	print(f'Count 1: {count_1}')
	print(f'Count 0: {count_0}')
	
print(' *          8          *            8            *')
print('            ')
print(' Task 1 Finished ')
print('            ')
print(' *          8          *            8            *')

# print(gamma)
# print(epsilon)

# power_consumption = int(gamma,2)*int(epsilon,2)
# print(power_consumption)

# Life Support Rating
# = oxygen_generator_rating * co2_scrubber_rating

# 1. Oxygen Generator Rating
print()
print('-----------')
print('Oxygen Generator Rating')
print('-----------')
lst_tuples_nums = [(count,num) for count,num in enumerate(processed)]

while (len(lst_tuples_nums)!=1):
	for digit in range(len(lines[0])-1):
		print(f'Iteration: {digit}')
		pos_ones = []
		pos_zeros = []
		for elem in lst_tuples_nums:
			if elem[1][digit] == '1':
				pos_ones.append(elem[0])
			else:
				pos_zeros.append(elem[0])
		if len(pos_ones)>=len(pos_zeros):
			lst_tuples_nums = [elem for elem in lst_tuples_nums 
								if elem[0] not in pos_zeros]
		else:
			lst_tuples_nums = [elem for elem in lst_tuples_nums 
								if elem[0] not in pos_ones]


print(f'Length of binary numbers: {len(lines[0])}')
oxygen_generator_rating = int(lst_tuples_nums[0][1],2)
print(lst_tuples_nums[0][1])
print(f'Oxygen Generator Rating: {oxygen_generator_rating}')


# 2. CO2 Scrubber Rating
print()
print('-----------')
print('CO2 Scrubber Rating')
print('-----------')
lst_tuples_nums = [(count,num) for count,num in enumerate(processed)]
# print(len(lst_tuples_nums))

while (len(lst_tuples_nums)!=1):
	for digit in range(len(lines[0])-1):
		print(f'Iteration: {digit}')
		pos_ones = []
		pos_zeros = []
		for elem in lst_tuples_nums:
			if elem[1][digit] == '1':
				pos_ones.append(elem[0])
			else:
				pos_zeros.append(elem[0])
		if len(pos_ones)<len(pos_zeros) and len(lst_tuples_nums)>len(pos_zeros):
			lst_tuples_nums = [elem for elem in lst_tuples_nums 
								if elem[0] not in pos_zeros]
		elif len(lst_tuples_nums)>len(pos_ones):
			lst_tuples_nums = [elem for elem in lst_tuples_nums 
								if elem[0] not in pos_ones]
		print(f'Length list: {len(lst_tuples_nums)}')

co2_scrubber_rating = int(lst_tuples_nums[0][1],2)
print(f'CO2 Scrubberr Rating: {co2_scrubber_rating}')

# RESULT:
result = oxygen_generator_rating*co2_scrubber_rating
print(result)





