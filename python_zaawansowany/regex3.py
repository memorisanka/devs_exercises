import re

mail = 'heniek.jakmutam@serwis.com'
company_name = re.findall(r"[a-zA-Z]+@([a-zA-z]+).com", mail)
print("Nazwa firmy: {}".format(company_name[0].title()))


txt = "5 dogs 3 cats 10 other pets"
digits = re.findall(r"\d+", txt)
print(digits)