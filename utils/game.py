from utils.player import Player
from utils.player import Deck



class Board:
    """
    Create Board class, defined by:
    :player_names which is a list of strings
    """
    def __init__(self, player_names: list[str]):
        self.deck = Deck()
        self.deck.shuffle() #shuffles the deck
        num_players = len(player_names) # count the number of players
        num_cards_per_player = len(self.deck.card) // num_players #divides the deck by the number of players
        self.players = [Player(name, self.deck.distribute(num_cards_per_player)) for name in player_names]
        self.turn_count = 0 #set starting turn count to0
        self.active_cards = [] #creates the empty list where active cards are stored
        self.history_cards = [] #created the empty list where played cards are added to history

    def start_game(self):
        """function that starts the game"""
        while any(player.card for player in self.players): #while function loops as long as players have cards
            self.turn_count += 1 #sets the turn counter to count
            self.active_cards = [player.play() for player in self.players] #each player plays their active cards
            self.history_cards.extend(self.active_cards) #adds the played cards to each players history
            print(f"Turn {self.turn_count}:") #prints what turn it is at the start of each turn
            for card in self.active_cards: #loops through active/played cards and displays them
                print(card)

