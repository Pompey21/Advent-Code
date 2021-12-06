"""
Hello, hello! This is the puzzle of Day 5!
Day 5: https://adventofcode.com/2021/day/5
"""

# helper functions
def str_2_int(lst_int):
	return [int(elem) for elem in lst_int]


# read file
with open('input.txt') as f:
	lines = [[str_2_int(coordinates.split(',')) for coordinates in line[:-1].split(' -> ')] for line in f.readlines()]

# generate dictionary
track_dict = {}
for line in lines:
	# line is always of length 2
	coordinates1 = line[0]
	coordinates2 = line[1]
	# column-y:
	if coordinates1[1] == coordinates2[1]:
		y_component = coordinates1[1]
		if coordinates1[0] < coordinates2[0]:
			for x_component in range(coordinates1[0],coordinates2[0]+1):
				pair = (x_component,y_component)
				if pair not  in track_dict.keys():
					track_dict[pair] = 1
				else:
					track_dict[pair] = track_dict.get(pair)+1
		else:
			for x_component in range(coordinates2[0],coordinates1[0]+1):
				pair = (x_component,y_component)
				if pair not  in track_dict.keys():
					track_dict[pair] = 1
				else:
					track_dict[pair] = track_dict.get(pair)+1
	# row-x:
	if coordinates1[0] == coordinates2[0]:
		x_component = coordinates1[0]
		if coordinates1[1] < coordinates2[1]:
			for y_component in range(coordinates1[1],coordinates2[1]+1):
				pair = (x_component,y_component)
				if pair not in track_dict.keys():
					track_dict[pair] = 1
				else:
					track_dict[pair] = track_dict.get(pair)+1
		else:
			for y_component in range(coordinates2[1],coordinates1[1]+1):
				pair = (x_component,y_component)
				if pair not  in track_dict.keys():
					track_dict[pair] = 1
				else:
					track_dict[pair] = track_dict.get(pair)+1

	# diagonals
	else:
		if coordinates1[0] > coordinates2[0]:
			
			start_x = coordinates1[0]
			if coordinates1[1] < coordinates2[1]: # we go from BOTTOM-LEFT -> TOP-RIGHT
				start_y = coordinates1[1]
				for decrement in range(abs(coordinates1[0]-(coordinates2[0])+1)):
					pair = (start_x-decrement,start_y+decrement)
					if pair not in track_dict.keys():
						track_dict[pair] = 1
					else:
						track_dict[pair] = track_dict.get(pair)+1
			elif coordinates1[1] > coordinates2[1]: # we go from TOP-LEFT -> BOTTOM-RIGHT
				start_y = coordinates1[1]
				for decrement in range(abs(coordinates1[0]-(coordinates2[0])+1)):
					pair = (start_x-decrement,start_y-decrement)
					if pair not in track_dict.keys():
						track_dict[pair] = 1
					else:
						track_dict[pair] = track_dict.get(pair)+1


		elif coordinates1[0] < coordinates2[0]:
			start_x = coordinates1[0]
			if coordinates1[1] < coordinates2[1]: # we go from BOTTOM-LEFT -> TOP-RIGHT
				start_y = coordinates1[1]
				for decrement in range(abs(coordinates1[0]-(coordinates2[0]+1))):
					pair = (start_x+decrement,start_y+decrement)
					if pair not in track_dict.keys():
						track_dict[pair] = 1
					else:
						track_dict[pair] = track_dict.get(pair)+1
			elif coordinates1[1] > coordinates2[1]: # we go from TOP-LEFT -> BOTTOM-RIGHT
				start_y = coordinates1[1]
				for decrement in range(abs(coordinates1[0]-(coordinates2[0]+1))):
					pair = (start_x+decrement,start_y-decrement)
					if pair not in track_dict.keys():
						track_dict[pair] = 1
					else:
						track_dict[pair] = track_dict.get(pair)+1	

# print()
# print(track_dict)

# check how many crossed twice
counter = 0
for key in track_dict.keys():
	if track_dict.get(key) >= 2:
		counter += 1
print(counter)

print()

# visualizer:
# for y in range(999):
# 	strs = ""
# 	for x in range(999):
# 		strs = strs + str(track_dict.get((x,y),'.'))
# 	print(strs)


		

















# [[float(y) for y in x] for x in l]