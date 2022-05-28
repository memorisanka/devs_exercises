def multiply(*args):
    """Funkcja wykonuje mnożenie podanych jako parametr argumentów"""

    multiply_num = 1
    for num in args:
        multiply_num *= num

    return multiply_num


print(multiply(2, 3, 4, (-2)))
