# -*- coding: UTF-8 -*-

from cell import *

ROWS = 3
COLS = 3

class Board:
	def __init__(self):
		self.cells = [[0 for c in range(COLS)] for r in range(ROWS)]
		for row in range(0, ROWS):
			for col in range(0, COLS):
				self.cells[row][col] = Cell()
				self.cells[row][col].content = EMPTY

	# Retorna true se o jogador passado como parametro ganhou
	def has_won(self, player):
		# verifica linhas
		for row in range(0, ROWS):
			if (self.cells[row][0].content == player and 
				self.cells[row][0].content == self.cells[row][1].content and 
				self.cells[row][1].content == self.cells[row][2].content):
				return True
		# verifica colunas 		
		for col in range(0, COLS):
			if (self.cells[0][col].content == player and 
				self.cells[0][col].content == self.cells[1][col].content and 
				self.cells[1][col].content == self.cells[2][col].content):
				return True
		# verifica diagonais		
		return ((self.cells[0][0].content == player and 
			self.cells[0][0].content == self.cells[1][1].content and 
			self.cells[1][1].content == self.cells[2][2].content)
			or (self.cells[0][2].content == player and 
			self.cells[0][2].content == self.cells[1][1].content and 
			self.cells[1][1].content == self.cells[2][0].content))

	# Retorna verdadeiro (true) se empatou
	def is_draw(self):
		for row in range(0, ROWS):
			for col in range(0, COLS):
				if self.cells[row][col].content == EMPTY:
					return False 
		return True			

	# Exibe o tabuleiro
	def show(self):
		for row in range(0, ROWS):
			for col in range(0, COLS):
				self.cells[row][col].paint()
				if col != COLS-1:
					print "|",
			print
			if row != ROWS-1:
				print "-----------"	

			