"""
Hello, hello! This is the puzzle of Day 4!
Day 4: https://adventofcode.com/2021/day/4
"""

with open('input.txt') as f:
	lines = f.readlines()

print(len(lines))
print(lines[1])

# numbers called at bingo
calls = [int(num) if num[1:]!='\n' else int(num[:2]) for num in lines[0].split(',')]
print(calls)

lines = lines[2:]
# print(lines)


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
# print((bingo_boards))

def tick_element(element,bingo_boards):
	for count1,board in enumerate(bingo_boards):
		for count2,row in enumerate(board):
			for count3,elem in enumerate(row):
				if elem[0] == element:
					elem_lst = list(elem)
					elem_lst[1] = 1
					elem = tuple(elem_lst)
					print(elem)
					print(row)
					row[count3] = elem
					board[count2] = row
					bingo_boards[count1] = board
			# print(row)
			# break
	return bingo_boards

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

bingo_boards = tick_element(49,bingo_boards)
print(bingo_boards)

