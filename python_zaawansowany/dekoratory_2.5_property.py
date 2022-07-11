class BankAccount:

    def __init__(self, number: int) -> None:
        self.__number = number

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, value: int):
        self.__number = value

    @number.deleter
    def number(self):
        del self.__number

    @number.getter
    def number(self):
        return self.__number


def main():
    account1 = BankAccount(12345)
    print(account1.number)
    account1.number = 775757755
    print(account1.number)
    del account1.number
    print(account1.number)


if __name__ == "__main__":
    main()
