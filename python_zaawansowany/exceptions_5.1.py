def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ValueError:
            print("Nieprawidłowe dane.")
        except ZeroDivisionError:
            print("Nie można dzielić przez zero.")


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    try:
        for i in range(len(L)):
            sumOfPairs.append(L[i] + L[i + 1])
        print("sumOfPairs = ", sumOfPairs)
    except ValueError:
        print("Błąd działania programu.")


def printUpperFile(fileName):
    global file
    try:
        file = open(fileName, "r")
        for line in file:
            print(line.upper())
    except (ValueError, FileExistsError, FileNotFoundError):
        print("Błąd działania programu.")
    finally:
        file.close()


def main():
    try:
        example1()
        L = [10, 3, 5, 6, 9, 3]
        example2(L)
        example2([10, 3, 5, 6, "NA", 3])
        example3([10, 3, 5, 6])
        printUpperFile("doesNotExistYest.txt")
        printUpperFile("./Dessssktop/misspelled.txt")
    except NameError:
        print("Błędna nazwa funkcji.")
    except (ValueError, SyntaxError):
        print("Błąd działania programu.")


if __name__ == "__main__":
    main()
