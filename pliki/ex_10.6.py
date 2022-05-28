def read_line():
    counter = 0
    with open("test.txt", "r") as file:
        while counter < 3:
            file.readline()
            counter += 1
        line = file.readline()
    return line


def read_line2():
    with open("test.txt", "r") as file:
        lines = file.readlines()
    return lines[3]


print(read_line())
print(read_line2())
