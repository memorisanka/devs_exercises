import random




class Deck:
    face_and_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    suite = ["Hearts", "Diamonds", "Clubs", "Spades"]
    def __init__(self):
        self.deck = []
        for num in self.face_and_number:
            for colour in self.suite:
                self.deck.append(Card(num, colour))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def show(self):
        for c in self.deck:
            print(c)


class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def show(self):
        print("{}, {}".format(self.suite, self.face))

    def __str__(self):
        return f"{self.suite}, {self.face}"


def main():
    deck1 = Deck()
    print(deck1.show())
    print(deck1.deck[0])
    print(len(deck1.deck))



if __name__ == "__main__":
    main()