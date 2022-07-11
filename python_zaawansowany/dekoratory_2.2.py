def add_stars(func):
    def inner(*args):
        print(20 * "*")
        func(*args)
        print(20 * "*")

    return inner

@add_stars
def print_something(txt):
    print(txt)


print_something("Jakiś tekst")