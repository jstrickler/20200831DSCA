import random


class CardDeck:  # CardDeck(object)
    SUITS = "Clubs Diamonds Hearts Spades".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, value):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer name must be a string")

    # @property
    # def wombat(self):
    #     return self._wombat
    #
    # @wombat.setter
    # def wombat(self, value):
    #     self._wombat = value

    # @property
    # def spam(self):
    #     return self._spam

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({self.dealer}, {len(self)})"

