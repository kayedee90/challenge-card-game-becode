from utils.card import Card

"""imports the Card class"""
import random

"""imports the random attribute"""


class Player:
    """ "Create player class defined by characteristics:
    :player_name which stores the name of each player
    :card which is a list of cards (imported from card.py)
    :turn_count which is an int starting a 0.
    :number_of_cards which is an int starting at 0.
    :history which is a list of cards that will contain all the cards played by the player.
    """
    def __init__(self, name, card, turn_count: int = 0, number_of_cards: int = 0, history=0):
        self.player_name = name
        self.card = card
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = [] #creates an empty list that adds the played cards to players history

    def play(self):
        card_number = random.choice(self.card) #plays a random card from the players hand
        self.card.remove(card_number) #remove the card from the players hand
        self.history.append(card_number) #adds the card to the players history
        self.turn_count += 1 #ups the players turn count by 1
        return f"{self.player_name} on turn {self.turn_count} played: {card_number.value} {card_number.icon}"


class Deck:
    """create Deck class"""
    def __init__(self):
        """define the variables in :colors , :icons , :values"""
        icons = {"♥": "Red", "♦": "Red", "♣": "Black", "♠": "Black"}
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.card = [Card(color, suit, value) for suit, color in icons.items() for value in values]

    def shuffle(self):
        """shuffles the deck"""
        random.shuffle(self.card)

    def distribute(self, num_cards):
        """deals the cards"""
        distribute_cards = self.card[:num_cards] #take the cards cards from the beginning of the deck
        self.card = self.card[num_cards:] #remove the distributed cards from the deck
        return distribute_cards
