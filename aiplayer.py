# -*- coding: UTF-8 -*-
# Uma IA muito simples, na verdade tem só um conjunto de jogadas pre definidas e tenta executa-las.

from cell import *
from board import *

class AiPlayer:
	preferred_moves = [
		[1, 1], [0, 0], [0, 2], [2, 0], [2, 2],
		[0, 1], [1, 0], [1, 2], [2, 1]
	]

	def __init__(self, board):
		self.board = board

	def move(self):
		for i in range(len(self.preferred_moves)):
			row = self.preferred_moves[i][0]
			col = self.preferred_moves[i][1]
			if (self.board.cells[row][col].content == Cell.EMPTY):
				return self.preferred_moves[i]
		return None
