import random

class Symbol:
    """Class defining symbols, Characterized by attributes:
    :color which is a string
    :icons which is a single character out of this list [♥, ♦, ♣, ♠].
    '"""
    def __init__(self, color: str, icon):
        self.color = color
        self.icon = icon

    

class Card(Symbol):
    """"
    Child Class of Symbol, defining cards, adding attribute: 
    :value which defines the card number
    """
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value



