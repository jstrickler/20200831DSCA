from carddeck import  CardDeck


class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        for j in range(1, 3):
            joker = j, 'Joker'
            self._cards.append(joker)
