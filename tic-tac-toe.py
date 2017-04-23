# -*- coding: utf-8 -*-

# Constantes para representar os tipos de jogadores
EMPTY = 0
CROSS = 1
NOUGHT = 2

# Constantes para representar varios estados do jogo
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

def playerMove(currentPlayer):
	print "Jogador 'X', entre com sua jogada (linha[1-3] coluna[1-3]): "
	
	row = int(raw_input(""))-1
	col = int(raw_input(""))-1

	if is_valid_input(row, col):
		board[row][col] = CROSS
	else:
		print "Movimento inválido!"	

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

# ------------- Jogo ----------------------------
currentPlayer = CROSS
# Execução main
playerMove(currentPlayer) # update currentRow and currentCol
#updateGame(currentPlayer, currntRow, currentCol) # update currentState
print_board()
