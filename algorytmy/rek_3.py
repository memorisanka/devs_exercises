list1 = []


def crush(n: int):
    list1.append(n)
    return crush(n + 10)

crush(10)