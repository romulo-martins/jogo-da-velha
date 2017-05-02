# -*- coding: UTF-8 -*-
# Minimax com poda alpha-beta

from cell import *
from board import *
#from game import *

class Minimax:
	def __init__(self, board):
		self.board = board

	def move(self):
		# TODO:
		return None

	# Função apenas para TESTE, remover apos conseguir implementar o Minimax	
	def do_move(self):
		print "Jogador 'O', entre com sua jogada (linha[1-3] coluna[1-3]): "
		row = int(raw_input())-1
		col = int(raw_input())-1		
		self.board.cells[row][col].content = Cell.NOUGHT	

	# Retorna uma lista de possiveis jogadas
	def legal_moves(self):
		moves = []
		for row in range(0, Board.ROWS):
			for col in range(0, Board.COLS):
				if self.board.cells[row][col].content == Cell.EMPTY:
					 moves.append([row, col])
		return moves

    # Retorna um valor para O; 1 para vencer, -1 para perder, 0 em caso contrario.    
    def utility(self, player):
    	if self.board.has_won(Cell.NOUGHT):
    		return 1
    	elif self.board.has_won(Cell.CROSS):
    		return -1
    	else:
    		return 0	 	

    # Retorna verdadeiro caso tenha terminado o jogo 
    def terminal_test(self):
        # TODO:
        return None	
