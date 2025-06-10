from utils.game import Board

import sys
sys.stdout.reconfigure(encoding='utf-8')
"""needed this for the card symbols to work"""

board = Board(["Player 1", "Player 2", "Player 3"]) #names all players playing the game
board.start_game() #starts the game
