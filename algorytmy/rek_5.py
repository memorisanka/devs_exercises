def calc_NWD(a: int, b: int) -> int:
    if b > a:
        a, b = b, a

    if b == 0:
        return a

    return calc_NWD(b, a % b)

def calc_NWW(a, b):
    return (a * b) / calc_NWD(a, b)

print(calc_NWW(2, 4))
print(calc_NWW(8, 16))
print(calc_NWW(4, 28))
print(calc_NWW(3, 38))
print(calc_NWW(2, 3))
print(calc_NWW(5, 10))
print(calc_NWW(6, 8))