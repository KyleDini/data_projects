from random import shuffle

class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
        # Card references the Card class that was created above, which is why it is outputted as ___ of ___

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.cards_remaining != 52:
            raise ValueError(f"Only full decks can be shuffled")

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)



d = Deck()
d.shuffle()
print(d.cards)
card = d.deal_card()
hand = d.deal_hand(5)

print(d.count())
print(card)
print(hand)