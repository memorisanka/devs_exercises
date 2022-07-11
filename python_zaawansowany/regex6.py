import re

txt = "#AB4745 #AC3 #CD3 #hhghhh ##886868685"
pattern = r"#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}"
find = re.findall(pattern, txt)

print(find)

txt = "#AB4745 #CD3 #886868685"
pattern = r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b"
find = re.findall(pattern, txt)

print(find)