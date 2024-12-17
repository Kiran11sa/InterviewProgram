s = "Kiranisagoodboysintheworld"
unique_chars = []

for char in s:
    if char not in unique_chars:
        unique_chars.append(char)

result = ''.join(unique_chars)
print(result)
