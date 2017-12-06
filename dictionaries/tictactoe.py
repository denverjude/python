# 2 player tictactoe game 

def printBoard(board):
	print(bintomove(board[0][0]) + '|' + bintomove(board[0][1]) + '|' + bintomove(board[0][2]))
	print('-+-+-')
	print(bintomove(board[1][0]) + '|' + bintomove(board[1][1]) + '|' + bintomove(board[1][2]))
	print('-+-+-')
	print(bintomove(board[2][0]) + '|' + bintomove(board[2][1]) + '|' + bintomove(board[2][2]))
	print()

def winner_check(board):
	top_row = board[0][0] + board[0][1] + board[0][2]
	mid_row = board[1][0] + board[1][1] + board[1][2]
	bot_row = board[2][0] + board[2][1] + board[2][2]
	left_col = board[0][0] + board[1][0] + board[2][0]
	mid_col = board[0][1] + board[1][1] + board[2][1]
	right_col = board[0][2] + board[1][2] + board[2][2]
	diagonal1 = board[0][0] + board[1][1] + board[2][2]
	diagonal2 = board[0][2] + board[1][1] + board[2][0]

	if top_row == 3:
		return 'X Winner'
	elif mid_row == 3:
		return 'X Winner'
	elif bot_row == 3:
		return 'X Winner'
	elif left_col == 3:
		return 'X Winner'
	elif mid_col == 3:
		return 'X Winner'
	elif right_col == 3:
		return 'X Winner'
	elif diagonal1 == 3:
		return 'X Winner'
	elif diagonal2 == 3:
		return 'X Winner'

	elif top_row == 0:
		return 'O Winner'
	elif mid_row == 0:
		return 'O Winner'
	elif bot_row == 0:
		return 'O Winner'
	elif left_col == 0:
		return 'O Winner'
	elif mid_col == 0:
		return 'O Winner'
	elif right_col == 0:
		return 'O Winner'
	elif diagonal1 == 0:
		return 'O Winner'
	elif diagonal2 == 0:
		return 'O Winner'
	else:
		return 'No winner yet'		
					
def movetobin(turn):
	if turn == 'X':
		return 1
	else:
		return 0

def bintomove(state):
	if state == 1:
		return 'X'
	elif state == 0:
		return 'O'
	else:
		return '5'	

def number(k,turn,theBoard):
	#print('number function')
	#print('k is' + str(k))
	if k == 1:
		#print('1 active')
		theBoard[0][0] = movetobin(turn)
		#print(theBoard[0][0])
	elif k == 2:
		#print('1 active')
		theBoard[0][1] = movetobin(turn)
		#print(theBoard[0][1])
	elif k == 3:
		#print('1 active')
		theBoard[0][2] = movetobin(turn)
		#print(theBoard[0][2])
	elif k == 4:
		#print('1 active')
		theBoard[1][0] = movetobin(turn)
		#print(theBoard[1][0])
	elif k == 5:
		#print('1 active')
		theBoard[1][1] = movetobin(turn)
		#print(theBoard[1][1])
	elif k == 6:
		#print('1 active')
		theBoard[1][2] = movetobin(turn)
		#print(theBoard[1][2])
	elif k == 7:
		#print('1 active')
		theBoard[2][0] = movetobin(turn)
		#print(theBoard[2][0])
	elif k == 8:
		#print('1 active')
		theBoard[2][1] = movetobin(turn)
		#print(theBoard[2][1])
	elif k == 9:
		#print('1 active')
		theBoard[2][2] = movetobin(turn)
		#print(theBoard[2][2])
	else:
		print('Not Valid')								


def legend():
	print('1' + '|' + '2' + '|' + '3')
	print('-+-+-')
	print('4' + '|' + '5' + '|' + '6')
	print('-+-+-')
	print('7' + '|' + '8' + '|' + '9')
	print()

print('Let\'s play Tic Tac Toe !!!' )
print("Enter number to place X/O on. X moves first")
legend()
theBoard = [[5,5,5],[5,5,5],[5,5,5]]
turn = 'X'
l=[]
while True:
	k=int(input("Enter the number, turn for " + turn + '\n' ))
	#print('k is ' + str(k) + ' and turn is ' + turn)
	#print(theBoard)
	if (k in l) | (k not in range(1,10)):
		print('Not valid')
		continue
	l.append(k)
	number(k,turn,theBoard)
	#print(theBoard)
	printBoard(theBoard)
	win_check=winner_check(theBoard)
	print(win_check + '\n')
	if win_check != 'No winner yet':
		break
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

print('Game Over')

