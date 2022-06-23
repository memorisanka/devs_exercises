# 1. Linked List
# a) Czy lista jest pusta
# b) rozmiar listy
# c) Pobranie elementu z listy
# d) Dodanie elementu do listy na poczatku, na koncu
# e) Usuwanie elementu z listy


# 2. Stos Implementacja stosu

# 3. Implementacja Kolejki

my_list = ['To','taka', 'sobie', 'przykładowa', 'lista', 15, 'elementów',
       	'o', 'różnych', 'typach', 'między', 'innymi', 'str', 'i', 'int']


def print_list(my_list: list):
    if not my_list:
        return
    print(str(my_list[0]) + "1")
    return print_list(my_list[1:])

print_list(my_list)



def narcissistic(value):
    values = list(str(value))
    print(values)
    n = len(values)
    result = 0
    for number in values:
        result += int(number) ** n
    return f'{value} is narcissistic' if result == value else f'{value} is not narcissistic'
print(narcissistic(371))