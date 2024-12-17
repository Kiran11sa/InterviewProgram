# Example Python Code for Pass by Reference vs. Value
# defining the function
def squar(my_list):
    '''''''This function will find the square of items in the list'''
    squares = []
    for l in my_list:
        squares.append(l ** 2)
        squares.append(l ** 3)
    return squares


# calling the defined function
my_list = [12,17, 52, 8];
my_result = squar(my_list)
print("Squares of the list are: ", my_result)