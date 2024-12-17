s = "ljfoisnfo8ksa49kdcnn3nk"
s_only_digits = ''.join([char for char in s if char.isdigit()])

print(s_only_digits)

# --------------------------------------
s = "ljfoisnfo8ksa49kdcnn3nk"
s_only_digits = ""

for char in s:
    if char.isdigit():
        s_only_digits += char

print(s_only_digits)
