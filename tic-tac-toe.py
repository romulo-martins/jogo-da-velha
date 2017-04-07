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

# Exibe a celula com o conteudo especifico
def print_cell(content):
	if content == CROSS:
		print "X",
	elif content == NOUGHT:
		print "O",
	else:
		print " ",	

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

# Execução main
print_board()
