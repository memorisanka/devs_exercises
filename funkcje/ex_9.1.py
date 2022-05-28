def fun1(lista):
    """Funkcja znajduje największy element w podanej jako parametr liście."""

    return lista.index(max(lista))


def fun2(list2):
    """Funkcja znajduje największy element w podanej jako parametr liście."""
    counter_list = []
    for counter, num in enumerate(list2):
        counter_list.append((num, counter))
    counter_list = sorted(counter_list, reverse=True)
    return counter_list[0][0]


nums = [4, 9, 8, 28, 50, 2]

print(fun1(nums))
print(fun2(nums))
