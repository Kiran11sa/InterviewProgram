s = "ljfoisnfo8ksa49kdcnn3nk"
s_only_digits = ''.join([char for char in s if char.isdigit()])

print(s_only_digits)

# --------------------------------------
s = "ljfoisnfo8ksa49kdcnn3nk"
s_only_digits = ""
s_l=[]

for char in s:
    if char.isdigit():
        s_only_digits += char
        s_l.append(char)

result=''.join(s_l)
print(s_only_digits)
print('pppppppp',s_l)
print('gggggggdf',result)
