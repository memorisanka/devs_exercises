rain_dict = {}
flag = True

while flag:
    user_data = input("Podaj miasto i ilość opadów: ")
    if user_data == "":
        flag = False
    else:
        rain = user_data.split(" ")
        if rain[0] in rain_dict.keys():
            rain_dict[rain[0]] += int(rain[1])
        else:
            rain_dict.update({rain[0]: int(rain[1])})
for key, value in rain_dict.items():
    print(key, value)
