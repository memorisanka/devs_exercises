def arg_check(arg):
    def check(func):
        def inner(*args):
            func(*args)
            print(f"Typ argumentu funkcji dekorującej to: {type(arg)}")
            if isinstance(arg, type(args[0])):
                print("Podane argumenty są tego samego typu.")
            else:
                print("Podane argumenty nie są tego samego typu.")
        return inner
    return check


@arg_check(arg=5.0)
def example(arg2):
    print(f"Typ argumentu funkcji example to: {type(arg2)}")

example("jakiś string")