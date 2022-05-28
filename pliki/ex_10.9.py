import json

#
# with open("data.json") as json_file:
#     data = json.load(json_file)
#     counter = 0
#     items_number = int(data["totalCount"])
#     new_data = "\n"
# while counter < items_number:
#     dn = data["imdata"][counter]["l1PhysIf"]["attributes"]["dn"]
#     new_data += dn
#     new_data += "     "
#     descr = data["imdata"][counter]["l1PhysIf"]["attributes"]["descr"]
#     new_data += descr
#     new_data += "                        "
#     speed = data["imdata"][counter]["l1PhysIf"]["attributes"]["speed"]
#     new_data += speed
#     new_data += "         "
#     mtu = data["imdata"][counter]["l1PhysIf"]["attributes"]["mtu"]
#     new_data += mtu
#     new_data += "\n"
#     counter += 1
#
#     print(new_data)
#
# menu = '''
# Interface status
# =======================================================================
# DN                                                Description           Speed        MTU
# ---------------------------------------------  -------------------   -----------   --------'''
#
# with open("data_json.txt", "w") as outfile:
#     outfile.writelines(menu)
#     outfile.writelines((new_data))



with open("data.json") as f:
    data = json.load(f)

print("Interface Status\n")
print("=" * 79)
print("{:<50}{:<20}{:<20}{:<20}".format("DN", "Description", "Speed", "MTU"))
print()
print("-" * 48, "-"* 19,  "-"* 19, "-"* 15,)
for row in data['imdata']:
    dn = row["l1PhysIf"]["attributes"]["dn"]
    description = row["l1PhysIf"]["attributes"]["descr"]
    speed = row["l1PhysIf"]["attributes"]["speed"]
    mtu = row["l1PhysIf"]["attributes"]["mtu"]
    print("{:<50}{:<20}{:<20}{:<20}".format(dn, description, speed, mtu))


