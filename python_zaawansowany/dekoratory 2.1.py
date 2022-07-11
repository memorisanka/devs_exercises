
def logged(func):
    def inner(*args):
        print(f"""You called function "{func.__name__}" {str(args)} it returned {func(*args)}""")

    return inner


@logged
def add(*args):
    return 3 + len(args)


add(4, 4, 4)

