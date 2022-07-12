orders = [
    ["34587", "Learning Python, Mark Lutz", 4, 40.95],
    ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3, 32.95],
    ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
]


def check(lst: list):
    for i in lst:
        if i[1] < 100.0:
            i[1] += 10
    return lst


pre_invoice = list(map(lambda x: [x[0], x[2] * x[3]], orders))
check(pre_invoice)
invoice = list(map(lambda x: (x[0], x[1]), pre_invoice))
print(invoice)
