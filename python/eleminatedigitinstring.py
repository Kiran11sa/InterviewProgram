s = "ljfoisnfo8ksa49kdcnn3nk"

# Use a list comprehension to eliminate digits
s_without_digits = ''.join([char for char in s if not char.isdigit()])

print(s_without_digits)
# -----------------------------------\
s = "ljfoisnfo8ksa49kdcnn3nk"
s_without_digits = ""

for char in s:
    if not char.isnumeric():
        s_without_digits += char

print(s_without_digits)
# ------------------------------------\
s = "ljfoisnfo8ksa49kdcnn3nk"
s_without_digits = ""

for char in s:
    if not char.isdigit():
        s_without_digits += char

print(s_without_digits)
