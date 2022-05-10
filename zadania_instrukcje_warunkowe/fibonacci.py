n = int(input("Podaj liczbę n: "))

first, second = 0, 1
count = 0

if n <= 0:
    print("Wprowadziłeś liczbę ujemną lub 0.")
elif n == 1:
    print(f"Fibonacci sequence: {first}")
else:
    print("Fibonacci sequence:")
    while count < n:
        print(first)
        nth = first + second
        first = second
        second = nth
        count += 1


def fib(n, second_last, last):
    if n-1 == 0:
        return second_last
    else:
        new_last = second_last + last
        second_last = last
        return fib(n-1, second_last, new_last)