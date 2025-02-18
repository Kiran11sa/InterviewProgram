# List containing various values
l1 = ['123', 'aa12', 'abc', 'a1b2', '123c']
# Empty list to store alphanumeric values
alphanumeric_values = []
# Loop through the list
for item in l1:
    # Check if the item is a string, contains only alphanumeric characters, and is not purely numeric
    if isinstance(item, str) and item.isalnum():
        alphanumeric_values.append(item)

# Print the alphanumeric values
print("Alphanumeric values:", alphanumeric_values)
