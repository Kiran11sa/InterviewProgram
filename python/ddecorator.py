'''Decorators are one of the most helpful and powerful tools of Python. These are used to modify
the behavior of the function. Decorators provide the flexibility to wrap another function to expand
the working of wrapped function, without permanently modifying it.
In Decorators, functions are passed as an argument into another function and then called inside
the wrapper function.
It is also called meta programming where a part of the program attempts to change another part
 of program at compile time.'''
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