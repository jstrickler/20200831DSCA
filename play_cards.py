from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Matilda")
print(d1)

# naughty!
# print(d1._dealer)

print(d1.dealer) # self is d1 in dealer()
# d1.get_dealer()  d1.set_dealer()

d2 = CardDeck("Ferdinand")
print(d2.dealer)  # self is d2 in dealer()

d1.dealer = "Hortense"
print(d1.dealer)

try:
    d1.dealer = 1234
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards)
for i in range(5):
    print(d1.draw())
print()

print(d2.get_ranks())
print(CardDeck.get_ranks())

print(len(d1))

j1 = JokerDeck("Patty")
j1.shuffle()
print("j1 len:", len(j1))
print("j1 cards:", j1.cards)


print(d1, d2, j1)

print(str(d1), str(d2))
