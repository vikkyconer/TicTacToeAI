
actions = (0,1,2,3,4,5,6,7,8)
score = 1
board = []
def print_board(board):

	print "The board look like this: \n"

	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',
			elif board[i*3+j] != -1:
				print board[i*3+j]-1,
			else:
				print ' ',

			if j != 2:
				print " | ",
		print

		if i != 2:
			print "-----------------"
		else:
			print

def print_instruction():
	print "Please use the following cell numbers to make your move"
	# print_board([2,3,4,5,6,7,8,9,10])


def get_input(turn, action):

	valid = False
	while not valid:
		try:
			if action in actions:
				return action
			else:
				# print "That is not a valid move! Please try again.\n"
				# print_instruction()
				return -1
		except Exception as e:
			# print action + " is not a valid move! Please try again.\n"
			print e
			return -1

def check_win(board):
	win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	for each in win_cond:
		try:
			if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
				return board[each[0]-1]
		except:
			pass
	return -1

def reset_game(msg):
	global board
	# print_board(board)
	print msg
	board = []
	setBoard()
	# print_board([2,3,4,5,6,7,8,9,10])


def setBoard():
	global board
	for i in range(9):
		board.append(-1)

def try_move(turn, action):
	user = get_input(turn, action)
	if(user == -1):
		return -1
	if board[user] != -1:
		# print "Invalid move! Cell already taken. Please try again.\n"
		return -1
	board[user] = 1 if turn == 'X' else 0
	return 0
