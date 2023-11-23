class Probas:
    @staticmethod
    def prob(x, *args):
        new_list = [element for element in x if any(arg in element for arg in args)]
        return len(new_list) / len(x)
    
    @staticmethod
    def custom_sort_key(card):
        suit_order = {'♠': 0, '♥': 1, '♦': 2, '♣': 3}
        rank_order = {'A':0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}

        suit, rank = card[-1], card[:-1]  # Fix here, use -1 to get the last character for the suit
        return (suit_order[suit], rank_order[rank], card)

    @staticmethod
    def possible(x, *args):
        new_list = [element for element in x if any(arg in element for arg in args)]
        new_list.sort(key=Probas.custom_sort_key)
        return new_list