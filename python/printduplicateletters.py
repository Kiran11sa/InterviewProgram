s = "Kiranisagoodboysintheworld"
duplicate_chars = []

for char in s:
    if s.count(char) > 1 and char not in duplicate_chars:
        print(s.count(char))
        duplicate_chars.append(char)

result = ''.join(duplicate_chars)
print(result)

