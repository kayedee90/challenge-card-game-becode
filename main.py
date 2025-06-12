from utils.game import Board
import sys
sys.stdout.reconfigure(encoding='utf-8')
"""needed this for the card symbols to work"""



num_players = int(input("How many players? ")) #choose number of players
Players = [input(f"Enter Player {i+1}'s name: ") for i in range(num_players)] #enter player names

board = Board(Players) #names all players playing the game
board.start_game() #starts the game
