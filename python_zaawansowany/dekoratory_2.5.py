"""Przykład użycia @staticmethod"""


class Animal:

    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1

    @staticmethod
    def counter():
        print(f"Liczba utworzonych zwierząt: {Animal.count}")
        return Animal.count



def main():
    elephant = Animal("Dumbo")
    lion = Animal("Simba")
    zebra = Animal("Zebra")

    Animal.counter()


if __name__ == "__main__":
    main()
