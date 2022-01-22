"""

Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.


Does it mean the classical deck of cards?
    Yes, 52 cards, 13 ranks, 4 suits


"""
import enum
import dataclasses


class Suit(enum.Enum):
    
    hearts = 1
    spades = 2
    diamonds = 3
    clubs = 4
    

class Rank(enum.Enum):
    
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    

@dataclasses.dataclass
class Card:
    rank: Rank
    suit: Suit
    
    
@dataclasses.dataclass
class Deck:
    cards: List[Card]


