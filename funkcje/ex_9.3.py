def fizz_buzz(num):
    """Funkcja sprawdza czy podana liczba jest podzielna przez 3, podzielna  przez 5 lub
    podzielna przez 3 i 5"""

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return num


print(fizz_buzz(22))
help(fizz_buzz(4))
