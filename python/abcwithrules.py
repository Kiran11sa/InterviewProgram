def genpatern():
    vowel = 'EIOU'  # Define vowels
    result = []  # Initialize result list
    multipler = 1  # Start multiplier at 1

    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":  # Iterate through the alphabet
        result.append(i * multipler)  # Append the current letter multiplied by multiplier
        if i in vowel:  # If the letter is a vowel
            multipler += 1  # Increment the multiplier
            continue

    return ''.join(result)  # Join the result list into a single string


# Generate and print the pattern
z = genpatern()
print(z)
print("-------------------------------------------------------------")


def generate_patt():
    pattern = ""
    vowels = ['E', 'I', 'O', 'U']  # Define vowels
    repeat_count = 1  # Start repeat count at 1

    for i in range(26):
        char = chr(65 + i)  # Get the current character (A-Z)

        if char in vowels:  # If the character is a vowel
            pattern += char  # Add it to the pattern as it is
            repeat_count += 1  # Increment the repeat count
        else:
            pattern += char * repeat_count  # Repeat the character based on repeat count

    return pattern


# Generate and print the pattern
print(generate_patt())

