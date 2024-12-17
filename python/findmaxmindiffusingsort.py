def find_max_min_difference(arr):
    if len(arr) < 2:
        return None, None  # Not enough elements in the array

    arr.sort()  # Sort the array in ascending order

    max_difference = arr[-1] - arr[0]  # Maximum difference is between the last and first elements

    min_difference = float('inf')  # Initialize minimum difference to positive infinity
    print(min_difference)
    # min_difference = arr[-1]-arr[-2]  # Initialize minimum difference to positive infinity

    for i in range(1, len(arr)):
        difference = arr[i] - arr[i - 1]
        if difference < min_difference:
            min_difference = difference

    return max_difference, min_difference

# Example usage:
my_array = [4, 7, 2, 10, 5, 9]
max_diff, min_diff = find_max_min_difference(my_array)
print(f"Maximum Difference: {max_diff}")
print(f"Minimum Difference: {min_diff}")
