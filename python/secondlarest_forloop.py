numbers = [32,45,65,87,78,99,88,91]

# Initialize first_max and second_max to negative infinity
first_max = second_max = 0
# first_max = second_max = float('-inf')


# Iterate through the list
for num in numbers:
    if num > first_max:
        # If the current number is greater than the first maximum,
        # update both first_max and second_max
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        # If the current number is greater than the second maximum
        # and not equal to the first maximum, update second_max
        second_max = num
print("The second largest number in the list is:", second_max)

# # Check if a second maximum exists (at least two distinct numbers in the list)
# if second_max != float('-inf'):
#     print("The second largest number in the list is:", second_max)
# else:
#     print("There is no second largest number in the list.")
