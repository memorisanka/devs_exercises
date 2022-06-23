def print_numbers(n: int):
    if n == 0:
        return
    print(n)
    return print_numbers(n - 1)


print_numbers(100)