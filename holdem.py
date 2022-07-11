import random
from itertools import product
from collections import Counter

values = "AKQJT98765432"
ranks = [
    "High Card",
    "One Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush",
]


class PokerHand:

    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        self.cards = hand.split()
        self.count = Counter(card[0] for card in self.cards)

    @property
    def order(self):
        card_values = [card[0] for card in self.cards]
        card_values.sort(key=lambda x: (self.count[x] * -1, values.index(x)))
        return "".join(card_values)

    @property
    def hand_type(self):
        is_straight = self.order in values or self.order == "A5432"
        is_flush = len(set(card[1] for card in self.cards)) == 1

        if is_straight and is_flush:
            return "Straight Flush"
        elif 4 in self.count.values():
            return "Four of a Kind"
        elif 3 in self.count.values() and 2 in self.count.values():
            return "Full House"
        elif is_flush:
            return "Flush"
        elif is_straight:
            return "Straight"
        elif 3 in self.count.values():
            return "Three of a Kind"
        elif list(self.count.values()).count(2) == 2:
            return "Two Pair"
        elif 2 in self.count.values():
            return "One Pair"
        else:
            return "High Card"

    def compare_with(self, other):
        result = ranks.index(self.hand_type) - ranks.index(other.hand_type)
        if result > 0:
            return "Win"
        elif result < 0:
            return "Loss"
        else:
            for i in range(5):
                result = values.index(self.order[i]) - values.index(other.order[i])
                if result < 0:
                    return "Win"
                elif result > 0:
                    return "Loss"
            return "Tie"


if __name__ == "__main__":
    deck = ["".join(card) for card in product(values, "CDHS")]
    random.shuffle(deck)
    hand1 = PokerHand(" ".join(deck[:5]))
    hand2 = PokerHand(" ".join(deck[5:10]))
    print(hand1.cards, hand1.count, hand1.hand_type, hand1.order)
    print(hand2.cards, hand2.count, hand2.hand_type, hand2.order)
    print(hand1.compare_with(hand2))
