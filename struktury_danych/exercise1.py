name = "Jan Nowak" # -> J.N
name_1 = "patrk gajda" # -> P.G
name_2 = "Ewa C" # -> E.C
name_3 = "P nowak" # -> P.N
name_4 = "Dawid golota" # -> D.G
name_5 = "nowak Jan"

x, y = [1, 3]
array = name.split()
print(array)
name, last_name = name.upper().split(" ")
print(f"{name[0]}.{last_name[0]}")
# print(f"{name_i[0][0].upper()}.{name_i[1][0].upper()}")


txt = "Good night Sam!"
a = "mSa"
b = "eJo"
c = "odnght"
mytable = txt.maketrans(a, b, c)
print(txt.translate(mytable))


