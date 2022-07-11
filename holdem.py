import random
from itertools import product
from collections import Counter
from functools import cached_property

values = "AKQJT98765432"
ranks = [
    "Straight Flush",
    "Four of a Kind",
    "Full House",
    "Flush",
    "Straight",
    "Three of a Kind",
    "Two Pair",
    "One Pair",
    "High Card",
]


class PokerHand:
    def __init__(self, hand):
        self.cards = hand.split()
        self.count = Counter(card[0] for card in self.cards)

    @cached_property
    def order(self):
        card_values = [card[0] for card in self.cards]
        card_values.sort(key=lambda x: (self.count[x] * -1, values.index(x)))
        result = "".join(card_values)
        return "5432A" if result == "A5432" else result

    @cached_property
    def hand_type(self):
        is_straight = self.order in values or self.order == "5432A"
        is_flush = len(set(card[1] for card in self.cards)) == 1

        if is_straight and is_flush:
            return 0
        elif 4 in self.count.values():
            return 1
        elif 3 in self.count.values() and 2 in self.count.values():
            return 2
        elif is_flush:
            return 3
        elif is_straight:
            return 4
        elif 3 in self.count.values():
            return 5
        elif list(self.count.values()).count(2) == 2:
            return 6
        elif 2 in self.count.values():
            return 7
        else:
            return 8

    def __eq__(self, other):
        return self.order == other.order

    def __gt__(self, other):
        if self == other:
            return False
        result = self.hand_type - other.hand_type
        if result < 0:
            return True
        elif result > 0:
            return False
        else:
            for i in range(5):
                result = values.index(self.order[i]) - values.index(other.order[i])
                if result < 0:
                    return True
                elif result > 0:
                    return False

    def __str__(self):
        return f"<PokerHand {ranks[self.hand_type]} {self.cards}>"

    def compare_with(self, other):
        if self == other:
            return "Tie"
        elif self > other:
            return "Win"
        else:
            return "Loss"


if __name__ == "__main__":
    deck = ["".join(card) for card in product(values, "CDHS")]
    random.shuffle(deck)
    hand1 = PokerHand(" ".join(deck[:5]))
    hand2 = PokerHand(" ".join(deck[5:10]))
    print(hand1)
    print(hand2)
    print(hand1.compare_with(hand2))

    examples = [
        "KS AS TS QS JS",
        "2H 3H 4H 5H 6H",
        "AS AD AC AH JD",
        "JS JD JC JH 3D",
        "2S AH 2H AS AC",
        "AS 3S 4S 8S 2S",
        "2H 3H 5H 6H 7H",
        "2S 3H 4H 5S 6C",
        "2D AC 3H 4H 5S",
        "AH AC 5H 6H AS",
        "2S 2H 4H 5S 4C",
        "AH AC 5H 6H 7S",
        "AH AC 4H 6H 7S",
        "2S AH 4H 5S KC",
        "2S 3H 6H 7S 9C",
    ]
    for h in examples:
        print(PokerHand(h))
