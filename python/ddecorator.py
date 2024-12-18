#
# def divide(x, y):  # here, we are creating a function and passing the parameter
#     print(x / y)  # Here, we are printing the result of the expression
#
#
# def outer_div(func):  # here, we are creating a function and passing the parameter
#     def inner(x, y):  # here, we are creating a function and passing the parameter
#         if x < y:
#             x, y = y, x
#             return func(x, y)  # here, we are returning a function with some passed parameters
#
#     return inner
#
#
# divide1 = outer_div(divide)
# divide1(2, 4)
# ------------------------------------------------------------------------------------------------------------------
def outer_div(func):     # here, we are creating a function and passing the parameter
    def inner(x,y):        # here, we are creating a function and passing the parameter
        if(x<y):
           x,y = y,x
           return func(x,y)       # here, we are returning the function with the parameters
    return inner
# Here, the below is the syntax of generator
@outer_div
def divide(x,y):      # here, we are creating a function and passing the parameter
     print(x/y)
divide(4,6)