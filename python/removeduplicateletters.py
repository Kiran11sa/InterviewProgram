s = "Kiran is a good boys in the world"
unique_chars = []

for char in s:
    if char not in unique_chars:
        unique_chars.append(char)

result = ''.join(unique_chars)
print(result)
