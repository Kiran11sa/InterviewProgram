def a_function(string):
    "This prints the value of length of string"
    return len(string)
    return string[:2] # first return statement will be executed


# Calling the function we defined
print("Length of the string Functions is: ", a_function("Functions"))
print("Length of the string Python is: ", a_function("Python"))