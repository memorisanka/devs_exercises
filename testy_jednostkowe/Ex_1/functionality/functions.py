from math import sqrt

def is_prime(N: int) -> bool:
    if N == 1:
        return False

    for i in range(2, int(sqrt(N) + 1)):
        if not N % i:
            return False

    return True