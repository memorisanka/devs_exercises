# def removeRepeat():
#     with open("powtorzenia.txt", "r", encoding="utf-8") as file:
#         # # odczytanie z pliku pojedynczych linii
#         # line1 = file.readline()
#         line2 = file.readline()
#         line3 = file.readline()
#         # podział każdej linii na pojedyncze słowa w liście
#         line1 = line1.split(" ")
#         line2 = line2.split(" ")
#         line3 = line3.split(" ")
#         # usunięcie powtórzeń
#         line1.pop(4)
#         line1.pop(6)
#         line2.pop(5)
#         line3.pop(2)
#         line3.pop(5)
#         # utworzenie z list słów stringów, które będzie można zapisać do pliku
#         line1_txt = ""
#         line2_txt = ""
#         line3_txt = ""
#         for word in line1:
#             line1_txt = line1_txt + word + " "
#         for word in line2:
#             line2_txt = line2_txt + word + " "
#         for word in line3:
#             line3_txt = line3_txt + word + " "
#
#     with open("powtorzenia1.txt", "w", encoding="utf-8") as file:
#         file.writelines(line1_txt)
#         file.writelines(line2_txt)
#         file.writelines(line3_txt)
#
#
# print(removeRepeat())

already_existed = set()
with open('powtorzenia.txt', 'r') as file:
    array = []
    for line in file:
        for word in line.split():
            if word not in already_existed:
                array.append(word)
                already_existed.add(word)
    print(" ".join(array))
