filter_out = """.,'"/&%()[]-_*~`|/"""
raw_text = "ERAY067 & MANSUR x AVİE x ORGANİZE x BATUFLEX x CHİKO - HMDL"
filtered_text = raw_text
for word in filter_out:
    if word in raw_text:
        filtered_text = filtered_text.replace(word,'')
filtered_text = filtered_text.lower().split()
fixed_spaces = ""
for word in filtered_text:
    fixed_spaces += word + " "

print(fixed_spaces)