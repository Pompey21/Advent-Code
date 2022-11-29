with open('input.txt') as f:
	# task 1:
	lines = [elem[:-1] for elem in f.readlines()]

print(lines)

lowest_points = []
for i in range(len(lines)):
	for j in range(len(lines[0])):
		if i == 0:
			# corner (left) -> 2 examples
			if j == 0:
				current = int(lines[i][j])
				right = int(lines[i][j+1])
				down = int(lines[i+1][j])
				if current < right and current < down:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)
			# corner (right) -> 2 examples
			elif j == len(lines[0])-1:
				current = int(lines[i][j])
				left = int(lines[i][j-1])
				down = int(lines[i+1][j])
				if current < left and current < down:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)
			else:
				current = int(lines[i][j])
				down = int(lines[i+1][j])
				right = int(lines[i][j+1])
				left = int(lines[i][j-1])
				if current < down and current<left and current<right:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)

		elif i == len(lines)-1:
			# corner (left) -> 2 examples
			if j == 0:
				current = int(lines[i][j])
				right = int(lines[i][j+1])
				up = int(lines[i-1][j])
				if current < right and current < up:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)
			elif j == len(lines[0])-1:
				current = int(lines[i][j])
				left = int(lines[i][j-1])
				up = int(lines[i-1][j])
				if current < left and current < up:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)
			else:
				current = int(lines[i][j])
				up = int(lines[i-1][j])
				right = int(lines[i][j+1])
				left = int(lines[i][j-1])
				if current < down and current<left and current<right:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)

		else:
			if j == 0:
				current = int(lines[i][j])
				right = int(lines[i][j+1])
				up = int(lines[i-1][j])
				down = int(lines[i+1][j])
				if current < right and current < up and current < down:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)
			elif j == len(lines[0])-1:
				current = int(lines[i][j])
				left = int(lines[i][j-1])
				up = int(lines[i-1][j])
				down = int(lines[i+1][j])
				if current < left and current < up and current < down:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)
			else:
				current = int(lines[i][j])
				left = int(lines[i][j-1])
				right = int(lines[i][j+1])
				up = int(lines[i-1][j])
				down = int(lines[i+1][j])
				if current < left and current < up and current < down and current < right:
					print(f'i: {i} and j: {j}')
					print(current)
					print(lines[i])
					lowest_points.append(current)

print()
print(lowest_points)
print()

result = sum(lowest_points) #+len(lowest_points)
print(result)



















