# Loop through the ASCII values of 'a' to 'z'
for i in range(26):
    # chr(97) gives 'a', chr(98) gives 'b', ..., chr(122) gives 'z'
    # ord('a') = 97, so we add i to get each subsequent character
    # letter = chr(97 + i)
    # print(f"({letter},{i+1})", end=", ")
    Letters = chr(65+i)
    # print(f"({Letters},{i+1})",end=',')
# Initialize an empty list to store the letter-number pairs
# letter_number_pairs = []
#
# # Loop through the ASCII values of 'a' to 'z'
# for i in range(26):
#     # chr(97) gives 'a', chr(98) gives 'b', ..., chr(122) gives 'z'
#     letter = chr(97 + i)
#     # Append the tuple (letter, index) to the list
#     letter_number_pairs.append((letter, i+1))
#
# # Print the list
# print(letter_number_pairs)
#
# # import string
# #
# # # Generate the list of tuples
# alphabet_list = [(letter, index + 1) for index, letter in enumerate(string.ascii_lowercase)]
#
# # Print the list
# print(alphabet_list)
#
# Initialize an empty list to store the letter-number pairs
letter_number_pairs = []

# Loop through the ASCII values of 'a' to 'z'
for i in range(26):
    # chr(97) gives 'a', chr(98) gives 'b', ..., chr(122) gives 'z'
    letter = chr(97 + i)
    # Append the tuple (letter, index) to the list
    letter_number_pairs.append((letter, i+1))
print(letter_number_pairs)
# Format the output as a list without quotes
formatted_list = [f"({letter},{index})" for letter, index in letter_number_pairs]
print(formatted_list)

# Print the list as a string with comma-separated values
print(f"[{', '.join(formatted_list)}]")

