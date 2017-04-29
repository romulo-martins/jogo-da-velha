# -*- coding: UTF-8 -*-

# Constantes para representar os tipos de jogadore CROSS/X ou NOUGHT/O
EMPTY = 0
CROSS = 1
NOUGHT = 2

class Cell:
	def __init__(self):
		self.content = EMPTY

	def paint(self):
		if self.content == CROSS:
			print "X",
		elif self.content == NOUGHT:
			print "O",
		else:
			print " ",	

