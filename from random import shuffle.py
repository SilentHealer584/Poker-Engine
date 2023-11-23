from random import shuffle
from Module_PROBA import Probas as P

deck = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','T♠','J♠','Q♠','K♠',
        'A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','T♥','J♥','Q♥','K♥',
        'A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','T♦','J♦','Q♦','K♦',
        'A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','T♣','J♣','Q♣','K♣']

community_cards = [] # ❂ Chip Symbol

hands = []

def chance(card):
    count = 0
    for cards in deck:
        count += cards.count(card)
    return count / len(deck)

def Shuffle(x):
    shuffle(x)

shuffle(deck)

print(deck)

print(P.prob(deck, "A", "3", "♣")) # CALCULE PROBAS EN UNION p.ex :      P.prob(deck, "♠", "9", "A", "♦") >>> 0.5769230769230769       OU INDIVIDUEL p.ex :      P.prob(deck, "♦") >>> 0.25
print(P.possible(deck, "A", "3", "♣")) # MONTRE LES CARTES POUVANT ETRE PIOCHEES EN FONCTION DES CRITERES p.ex :    P.possible(deck, "A", "5") >>> ['A♠', '5♠', 'A♥', '5♥', 'A♦', '5♦', 'A♣', '5♣']