# odczytanie danych z pliku
with open("pixel.txt", "r") as file:
    pixels = file.readlines()
# utworzenie ciągu znaków z otrzymanej poleceniem readlines() listy
pixels_str = ""
counter = 0
while counter < len(pixels):
    for i in pixels:
        pixels_str += i
        counter += 1
# zamiana znaku nastepnej lini na spację
pixels_str = pixels_str.replace("\n", " ")
# utworzenie listy liczb w formacie str za pomocą funkcji split()
pixel_list = pixels_str.split(" ")
# usunięcie pustych stringów i tych, które są spacją
for num in pixel_list:
    if num == " " or num == "":
        pixel_list.remove(num)
# zamiana str na int
pixels_num = []
for num in pixel_list:
    pixels_num.append(int(num))
# znalezienie wartości maksymalnej i minimalnej w liście pixels_num
max_pixel = max(pixels_num)
print(max_pixel)
min_pixel = min(pixels_num)
print(min_pixel)


with open("pixels_answers.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(f"Odpowiedź do zadania 10.1:\n\n")
    outfile.writelines(f"Jasność najciemniejszego piksela to: {min_pixel}\n")
    outfile.writelines(f"Jasność najjaśniejszego piksela to: {max_pixel}\n")
