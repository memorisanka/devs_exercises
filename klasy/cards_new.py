import collections
Card = collections.namedtuple('Card',['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        import random
        random.shuffle(self._cards)

    def play(self):
        if len(self) == 0:
            return
        return self._cards.pop()





def main():
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])


if __name__ == "__main__":
    main()
