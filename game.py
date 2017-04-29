# -*- coding: UTF-8 -*-

from cell import *
from board import *

# Constantes para representar varios estados do jogo, vai para variavel game_state
PLAYING = 0
DRAW = 1
CROSS_WON = 2
NOUGHT_WON = 3

class Game:

	def __init__(self):
		self.board = Board()

	# Método que dá inicio ao jogo em si	
	def play(self):
		self.init_game()
		self.board.show()
		while self.game_state == PLAYING:
			self.player_move(self.current_player)
			self.board.show()
			self.update_game(self.current_player)
			self.show_game_status(self.game_state)	
			self.current_player = NOUGHT if self.current_player == CROSS else CROSS

	def init_game(self):
		print "Olá, vamos começar a jogar"	
		self.current_player = self.choose_player()
		self.game_state = PLAYING

	# Verifica se uma jogada válida	
	def is_valid_input(self, row, col):
		return ((row >= 0) and (row < ROWS) and (col >= 0) and (col < COLS) and 
			(self.board.cells[row][col].content == EMPTY))

	# Verifica se o campo digitado foi x/X
	def is_cross(self, value):
		return value == 'x' or value == 'X'	

	# verifica se o campo digitado foi o/O	
	def is_nought(self, value):
		return value == 'o' or value == 'O'	

	# Método para escolher se o jogador quer jogar com X ou O
	def choose_player(self):
		while(True):
			print "Escolha quem começa X ou O (x/o): "
			player = str(raw_input())
			if self.is_cross(player):
				return CROSS
			elif self.is_nought(player):
				return NOUGHT	
			else:
				print "Opção inválida!"

	# O jogador do estado atual executa seu movimento
	def player_move(self, player):
		if player == CROSS:
			print "Jogador 'X', entre com sua jogada (linha[1-3] coluna[1-3]): "
		else:
			print "Jogador 'O', entre com sua jogada (linha[1-3] coluna[1-3]): "		

		valid_input = False
		while not valid_input:
			row = int(raw_input())-1
			col = int(raw_input())-1

			if self.is_valid_input(row, col):
				self.board.cells[row][col].content = player	
				valid_input = True		
			else:
				print "Movimento inválido! Tente novamente: "	

	def update_game(self, player):
		if(self.board.has_won(player)):
			self.game_state = CROSS_WON if player == CROSS else NOUGHT_WON
		elif(self.board.is_draw()):
			self.game_state = DRAW

	def show_game_status(self, game_state):
		if game_state == NOUGHT_WON:
			print "Vencedor O!\n Fim de Jogo!"
		elif game_state == CROSS_WON:
			print "Vencedor X!\n Fim de Jogo!"
		elif game_state == DRAW:	
			print "Empate!\n Fim de Jogo"		
							

# ------------- Jogo ----------------------------
g = Game()	
g.play()