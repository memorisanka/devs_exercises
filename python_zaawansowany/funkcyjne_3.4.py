lines = ["10000101011", "111111", "01010101010010", "011001100001", "001010101011"]


def counter(lst: list):
    count = list(filter(lambda x: x.count("11"), lst))
    return f"Wynik: {set(lst) - set(count)}"


print(counter(lines))
