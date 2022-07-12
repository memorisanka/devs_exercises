def add_stars(func):
    def inner(*args):
        print(30 * "*")
        func(*args)
        print(30 * "*")

    return inner

@add_stars
def print_something(txt):
    print(txt)


print_something("Szedł Grześ przez wieś.")