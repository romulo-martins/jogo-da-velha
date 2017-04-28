# -*- coding: utf-8 -*-

# Constantes para representar os tipos de jogadores, vai para variavel current_player
EMPTY = 0
CROSS = 1
NOUGHT = 2

# Constantes para representar varios estados do jogo, vai para variavel game_state
PLAYING = 0
DRAW = 1
CROSS_WON = 2
NOUGHT_WON = 3

# O Tabuleiro do jogo e o status do jogo
ROWS = 3 # numero de linhas do tabuleiro
COLS = 3 # numero de colunas do tabuleiro
board = [[EMPTY, EMPTY, EMPTY],
		[EMPTY, EMPTY, EMPTY],
		[EMPTY, EMPTY, EMPTY,]]

# ---------- Métodos ------------------

def is_even(number):
	return number % 2 == 0

def is_valid_input(row, col):
	return (row >= 0) and (row < ROWS) and (col >= 0) and (col < COLS) and (board[row][col] == EMPTY)

def is_cross(value):
	return value == 'x' or value == 'X'	

def is_nought(value):
	return value == 'o' or value == 'O'

#  Retorna verdadeiro (true) se empatou
def is_draw():
	for row in range(0, ROWS):
		for col in range(0, COLS):
			if board[row][col] == EMPTY:
				return False 
	return True			

def player_is_valid(player):
	return player == CROSS or player == NOUGHT	

# O jogador do estado atual executa seu movimento
def player_move(current_player):
	if current_player == CROSS:
		print "Jogador 'X', entre com sua jogada (linha[1-3] coluna[1-3]): "
	else:
		print "Jogador 'O', entre com sua jogada (linha[1-3] coluna[1-3]): "		

	valid_input = False
	while not valid_input:
		row = int(raw_input())-1
		col = int(raw_input())-1

		if is_valid_input(row, col):
			if current_player == CROSS:
				board[row][col] = CROSS
			else:
				board[row][col] = NOUGHT	
			valid_input = True		
		else:
			print "Movimento inválido! Tente novamente: "	


# Verifica se existe um vencedor
def has_won():
	# verifica linhas
	for row in range(0, ROWS):
		if board[row][0] != EMPTY and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
			return True

	# verifica colunas 		
	for col in range(0, COLS):
		if board[0][col] != EMPTY and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
			return True

	if (board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
		return True

	if (board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
		return True		

	return False		
			
# Exibe o tabuleiro
def print_board():
	for row in range(0, ROWS):
		for col in range(0, COLS):
			print_cell(board[row][col])
			if col != COLS-1:
				print "|",
		print
		if row != ROWS-1:
			print "-----------"

# Exibe a celula com o conteudo especifico
def print_cell(content):
	if content == CROSS:
		print "X",
	elif content == NOUGHT:
		print "O",
	else:
		print " ",	

# Método para escolher se o jogador quer jogar com X ou O
def choose_player():
	print "Escolha quem começa X ou O (x/o): "
	how_start = str(raw_input())
	if is_cross(how_start):
		return CROSS
	elif is_nought(how_start):
		return NOUGHT
	return EMPTY	

def update_game():
	if has_won() and current_player == CROSS:
		print "Jogador O vencedor!"
		return NOUGHT_WON
	elif has_won() and current_player == NOUGHT:
		print "Jogador X vencedor!"
		return CROSS_WON
	elif is_draw():	
		print "Empatou!"
		return DRAW
	else:
		return PLAYING			


# ------------- Jogo ----------------------------
current_player = EMPTY
exit = False
while(not exit):
	current_player = choose_player()
	if not player_is_valid(current_player):
		print "Opção inválida!"
	else:
		exit = True	

game_state = PLAYING
print_board()
while game_state == PLAYING:
	player_move(current_player)
	current_player = NOUGHT if current_player == CROSS else CROSS
	print_board()
	game_state = update_game()
