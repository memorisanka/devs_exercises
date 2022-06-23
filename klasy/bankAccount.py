# klasa python o nazwie BankAccount, ona bedzie reperezntowacd konto bankowe i bedzie miec nastepujace atrybuty :
# account_number(typLiczbowy), name(string), balance(float) -> Konstrktor
# deposit wplaty
# withdraw wyplaty -> Czy jest mozliwosc wyplaty takich srodkow
# bank_fees stosowac oplaty stale wysokosci 5%
# display czyli szczegoly konta
# przy depozycie i wyplacie weryfikacja pinu. Osobna metoda
# metoda realizujaca przelew do innego uzytkownika
import random
class Bank:
    accounts = []



class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float, pin: str):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.pin = pin
        self.account_number
        Bank.accounts.append(self)


    def deposit(self) -> float:
        """Pobiera od użytkownika kwotę wpłaty i dodaje ją do salda."""
        BankAccount.pin_verification(self)
        how_much_to_deposit = float(input("Ile gotówki chcesz wpłacić?: "))
        self.balance += how_much_to_deposit
        print(f"Wpłacono: {how_much_to_deposit} PLN. Aktualny stan konta: {self.balance} PLN.")
        return self.balance

    def withdraw(self) -> float:
        """Pobiera od użytkownika kwotę do wypłaty i, jeśli sa środki, odejmuje ja od salda."""
        BankAccount.pin_verification(self)
        how_much_to_withdraw = float(input("Ile gotówki chcesz wypłacić?: "))
        if how_much_to_withdraw > self.balance:
            print("Brak wystarczających środków.")
        else:
            self.balance -= how_much_to_withdraw
            print(f"Wypłacono: {how_much_to_withdraw} PLN. Aktualny stan konta: {self.balance} PLN.")
        return self.balance

    def bank_fees(self) -> float:
        """Pobiera od użytkownika miesięczną opłatę w wysokości 5% wartości konta"""
        new_balance = self.balance * 0.95
        return new_balance

    def display(self) -> None:
        """Wyświetla aktualne szczegóły konta."""
        print("Szczegóły konta:")
        print(f"Numer konta: {self.account_number}")
        print(f"Nazwa użytkownika: {self.name}")
        print(f"Aktualny stan konta: {self.balance} PLN")

    def pin_verification(self) -> None:
        """Weryfikacja, czy wprowadzony pin jest prawidłowy."""
        user_pin = input("Podaj pin: ")
        if user_pin == self.pin:
            print("PIN poprawny.")
        else:
            print("Błędny PIN.")
            print("*" * 50)
            BankAccount.menu(self)

    def pin_change(self) -> str:
        """Metoda pozwalająca zmienić pin użytkownika po weryfikacji starego pinu."""
        pin_ver = input("Podaj aktualny PIN: ")
        if pin_ver == self.pin:
            new_pin = input("Podaj nowy PIN: ")
            self.pin = new_pin
            print("PIN został zmieniony.")
            return self.pin
        else:
            print("Błędny PIN.")
            print("*" * 50)
            BankAccount.menu(self)

    def money_transfer(self, account_number):
        # TODO czy istnieje
        #
        transfer = float(input("Jaką kwotę chcesz przelać? "))
        user = input("Podaj nazwę odbiorcy przelewu: ")
        if transfer > self.balance:
            print("Brak wystarczających środków na koncie.")
            BankAccount.menu(self)
        else:
            self.balance -= transfer
            account.balance += self.balance

        #   TODO: wymyślić, jak przelać kasę innemu użytkownikowi

    def menu(self):
        """Wyświetla menu, w którym użytkownik wybiera, co chce dalej zrobić."""
        menu = """
        MENU
        -----------------------------------
        1 - Szczegóły konta
        2 - Wpłata środków na konto
        3 - Wypłata środków z konta
        4 - Aktualny stan konta
        5 - Przelew do innego użytkownika
        6 - Zmiana pinu
        7 - Wyloguj
        -----------------------------------"""
        print(menu)
        choice = int(input("Wybierz opcję (1-6): "))
        if choice == 1:
            BankAccount.display(self)
            BankAccount.menu(self)
        elif choice == 2:
            BankAccount.deposit(self)
            BankAccount.menu(self)
        elif choice == 3:
            BankAccount.withdraw(self)
            BankAccount.menu(self)
        elif choice == 4:
            print(f"Aktualny stan konta: {self.balance} PLN.")
            BankAccount.menu(self)
        elif choice == 5:
            BankAccount.money_transfer(self)
            BankAccount.menu(self)
        elif choice == 6:
            BankAccount.pin_change(self)
            BankAccount.menu(self)
        elif choice == 7:
            print("Wylogowano")
        else:
            print("Błędne dane.")
            BankAccount.menu(self)


def main():
    joanna = BankAccount("37747477757757575", "Joanna", 100, "1234")
    monika = BankAccount("86886868868686886", "Monika", 50, "2345")
    joanna.menu()
    monika.menu()


if __name__ == "__main__":
    main()


