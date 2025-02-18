s = "Kiranisagoodboysintheworld"
duplicate_chars = []

for char in s:
    if s.count(char) > 1 and char not in duplicate_chars:
        print(f"{char}:",s.count(char))
        duplicate_chars.append(char)

result = ''.join(duplicate_chars)
print(result)
# for char in s:
#     if char in s:
#         duplicate_chars.append(char)
# print(duplicate_chars)

