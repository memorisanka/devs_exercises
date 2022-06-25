# dodaj rekurencyjnie wartość 1 do każdego elementu listy

my_list = ['To', 'taka', 'sobie', 'przykładowa', 'lista', 15, 'elementów',
       	'o', 'różnych', 'typach', 'między', 'innymi', 'str', 'i', 'int']


def print_list(my_list: list):
    if not my_list:
        return
    print(str(my_list[0]) + "1")
    return print_list(my_list[1:])

print_list(my_list)


