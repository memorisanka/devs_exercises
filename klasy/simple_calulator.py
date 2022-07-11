class Calculator:
    """"Prosty kalkulator"""

    def __init__(self) -> None:
        pass

    def handle_instruction(self) -> tuple[str, str]:
        """Przyjęcie liczb od użytkownika."""

        self.a = input("Podaj pierwszą liczbę: ")
        self.b = input("Podaj drugą liczbę: ")
        return self.a, self.b

    def what_to_do(self) -> None:
        """Określenie przez użytkownika, jakie działanie chce wykonać."""

        to_do = input("Jakie działanie chcesz wykonać? (+, -, *, /) or q(quit): ")
        match to_do:
            case "+":
                Calculator.handle_instruction(self)
                Calculator.sum(self)
            case "-":
                Calculator.handle_instruction(self)
                Calculator.subtract(self)
            case "*":
                Calculator.handle_instruction(self)
                Calculator.multiply(self)
            case "/":
                Calculator.handle_instruction(self)
                Calculator.divide(self)
            case "q":
                print("Koniec działania programu.")

    def sum(self) -> int:
        """Metoda, która dodaje do siebie podane argumenty."""

        try:
            sum_result = int(self.a) + int(self.b)
        except (TypeError, ValueError):
            print("Błędne dane.")
            return 0
        else:
            print(f"Wykonywane działanie: {self.a} + {self.b}")
            print(f"Wynik działania: {sum_result}")
            return sum_result

    def subtract(self) -> int:
        """Metoda, która odejmuje od siebie podane argumenty."""

        try:
            subtract_result = int(self.a) - int(self.b)
        except (TypeError, ValueError):
            print("Błędne dane")
            return 0
        else:
            print(f"Wykonywane działanie: {self.a} - {self.b}")
            print(f"Wynik działania: {subtract_result}")
            return subtract_result

    def multiply(self) -> int:
        """Metoda, która mnoży podane argumenty."""

        try:
            multiply_result = int(self.a) * int(self.b)
        except (TypeError, ValueError):
            print("Błędne dane")
            return 0
        else:
            print(f"Wykonywane działanie: {self.a} * {self.b}")
            print(f"Wynik działania: {multiply_result}")
            return multiply_result

    def divide(self) -> float:
        """Metoda, która dzieli podane argumenty. Metoda sprawdza, czy użytkownik nie dzieli przez 0."""

        print(f"Wykonywane działanie: {self.a} / {self.b}")
        try:
            division_result = int(self.a) / int(self.b)
        except (ZeroDivisionError, TypeError, ValueError):
            print("Błędne dane lub dzielisz przez 0.")
            return 0
        else:
            print(f"Wykonywane działanie: {self.a} / {self.b}")
            print(f"Wynik działania: {division_result}")
            return division_result


def main():
    calc = Calculator()
    calc.what_to_do()


if __name__ == "__main__":
    main()
