# -*- coding: UTF-8 -*-
# Minimax com poda alpha-beta

from cell import *
from board import *

class Minimax:
	def __init__(self, board):
		self.board = board

	def move(self):
		m = self.minimax_decision(self.board.copy())
		return m[1]

	def minimax_decision(self, board):
		return self.max_value(board)

	# Minimiza a jogada do oponente	
	def min_value(self, board):
		if self.terminal_test(board):
			return [self.utility(board), None]
		v = [float("inf"), None]
		moves = self.legal_moves(board)
		for i in range(0, len(moves)):
			b = board.copy()			
			self.make_move(moves[i], b, Cell.CROSS)
			m = self.max_value(b) 
			if m[0] < v[0]:
				v[0] = m[0]
				v[1] = moves[i]
		return v

	# Maximiza a jogada do PC	
	def max_value(self, board):
		if self.terminal_test(board):
			return [self.utility(board), None]
		v = [float("-inf"), None]
		moves = self.legal_moves(board)
		for i in range(0, len(moves)):
			b = board.copy()
			self.make_move(moves[i], b, Cell.NOUGHT)
			m = self.min_value(b) 
			if m[0] > v[0]:
				v[0] = m[0]
				v[1] = moves[i]
		return v	

	# Executa a ação (a jogada)	
	def make_move(self, move, board, player):
		board.cells[move[0]][move[1]].content = player

	# Retorna uma lista de possiveis jogadas
	def legal_moves(self, board):
		moves = []
		for row in range(0, Board.ROWS):
			for col in range(0, Board.COLS):
				if board.cells[row][col].content == Cell.EMPTY:
					 moves.append([row, col])
		return moves

    # Retorna um valor para computador; 1 para vencer, -1 para perder, 0 em caso contrario.    
	def utility(self, board):
		if board.has_won(Cell.NOUGHT):
			return 1
		elif board.has_won(Cell.CROSS):
			return -1
		else:
			return 0	 	

	# Retorna verdadeiro caso tenha terminado o jogo 
	def terminal_test(self, board):
		return (board.is_draw() or board.has_won(Cell.NOUGHT) or board.has_won(Cell.CROSS))

