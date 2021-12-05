"""
Hello, hello! This is the puzzle of Day 4!
Day 4: https://adventofcode.com/2021/day/4
"""

with open('input.txt') as f:
	lines = f.readlines()

# numbers called at bingo
calls = [int(num) if num[1:]!='\n' else int(num[:2]) for num in lines[0].split(',')]
lines = lines[2:]

def prepare_bingo(lines):
	lines = [line for line in lines if line!='\n']
	counter=0
	bingo_boards=[]
	board = []
	for count,elem in enumerate(lines):
		if count % 5 == 0:
			bingo_boards.append(prepare_board(board))

			board = []
		board.append(elem)
	bingo_boards = [board for board in bingo_boards if board !=[]]
	return bingo_boards

def prepare_board(board):
	board = [[(int(elem),0) for elem in row.split()] for row in board]
	return board

bingo_boards = prepare_bingo(lines)

def tick_element(element,bingo_boards):
	list_changes = []
	for count1,board in enumerate(bingo_boards):
		for count2,row in enumerate(board):
			for count3,elem in enumerate(row):
				if elem[0] == element:
					elem_lst = list(elem)
					elem_lst[1] = 1
					elem = tuple(elem_lst)
					row[count3] = elem
					board[count2] = row
					bingo_boards[count1] = board

					# adding the locational information
					list_changes.append([count1,count2,count3])
	return bingo_boards,list_changes

def is_bingo(bingo_boards,location):
	# print(location)
	board = bingo_boards[location[0]]
	row = board[location[1]]
	# 1.
	# is row complete
	row_tick = [elem[1] for elem in row]
	if sum(row_tick)==len(row):
		return True,board
	# 2.
	# is column complete
	column_tick = [row[location[2]][1] for row in board]
	if sum(column_tick)==len(row):
		return True,board
	return False,[[],[],[],[],[]]

def sum_unmarked(board):
	result = 0
	for row in board:
		for elem in row:
			if elem[1]==0:
				result += elem[0]
	return result

def bingo(bingo_boards,calls):
	for number in calls:
		bingo_boards,list_changes = tick_element(number,bingo_boards)
		for location in list_changes:
			bool_val,board = is_bingo(bingo_boards,location)
			if bool_val==True:
				summation = sum_unmarked(board)
				return summation*number,list_changes[0]
	return 0,0

result,board_num = bingo(bingo_boards,calls)
print(result)

# For puzzle 2!
def bingo_2(bingo_boards,calls):
	counter = 0
	while (counter < len(bingo_boards)):
		for number in calls:
			bingo_boards,list_changes = tick_element(number,bingo_boards)
			for location in list_changes:
				bool_val,board = is_bingo(bingo_boards,location)
				if bool_val==True:
					counter+=1
					print(f'counter: {counter}')
					bingo_boards[location[0]] = []
					if counter==len(bingo_boards):
						print(f'Last number: {number}')
						summation = sum_unmarked(board)
						return summation*number,board
	return 0,0

result,board = bingo_2(bingo_boards,calls)
print(result)
print(board)





# bingo_boards,list_changes = tick_element(49,bingo_boards)




# test_board = [
# [[(1,1),(2,1),(3,1),(4,1),(5,1)],
# [(1,1),(2,0),(3,0),(4,0),(5,0)],
# [(1,1),(2,0),(3,0),(4,0),(5,0)],
# [(1,1),(2,0),(3,0),(4,0),(5,0)],
# [(1,0),(2,0),(3,0),(4,0),(5,0)]]
# ]

# test_loaction = [0,0,0]
# print()
# bool_val,board,last_elem = is_bingo(test_board,test_loaction)
# print(bool_val)
# print(board)


# summation = sum_unmarked(board)*last_elem
# print(summation)














