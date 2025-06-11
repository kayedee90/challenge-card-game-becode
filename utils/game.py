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
        self.turn_count = 0 #set starting turn count to 0
        self.active_cards = [] #creates the empty list where active cards are stored
        self.history_cards = [] #created the empty list where played cards are added to history

    def start_game(self):
        while any(player.card for player in self.players):  #while players have cards:
            self.turn_count += 1 #add to turn count

            
            played = [player.play() for player in self.players] #each player plays a card
            self.active_cards = [card for card, _ in played]
            messages = [msg for _, msg in played] #displays the card played

            winning_card = max(self.active_cards, key=lambda card: card.value) #determines the winning card

            for player, card in zip(self.players, self.active_cards):
                if card == winning_card:
                    player.score += 1 #adds a point to the player with the winning card
            self.history_cards.extend(self.active_cards) #adds played cards to history

            """prints turn messages"""
            print(f"Turn {self.turn_count}:") #turn message
            for msg in messages:
                print(msg)
            print(f"Winner of this turn: {winning_card.value} {winning_card.icon}\n") #winner of turn message

        winner = max(self.players, key=lambda player: player.score)
        print(f"Game Over! The winner is {winner.player_name} with {winner.score} points.**") #game ending message with final winner