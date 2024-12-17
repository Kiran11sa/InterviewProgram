n = [11, 2, 8, 3,10, 4, 5, 6]

largest_number = n[0] # Initialize largest_number with the first element

for num in n:
    if num > largest_number:
        largest_number = num

print("The largest number in the list is:", largest_number)
