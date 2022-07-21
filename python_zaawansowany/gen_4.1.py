def multiply():
    num = 1
    while True:
        yield num * 3
        num += 2


generator = multiply()
print(next(generator))
print(next(generator))
print(next(generator))
print(generator.__next__())
print(generator.__next__())

for i in range(15):
    print(next(generator))
