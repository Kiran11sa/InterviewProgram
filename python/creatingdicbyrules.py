"""The map() function in Python is a built-in functional programming tool used to apply a specified
function to each item in an iterable (like a list, tuple, or set) and
returns a map object (which can be converted to a list, tuple, etc.).

Syntax:
map(function, iterable)"""
numbers=[135,8,210,180,7,300,18]
result=sorted(map(lambda x:f"priority:{x}",filter(lambda x:x%3==0,numbers)),key=lambda l:len(l),reverse=True)
result1=sorted(map(lambda x:f"priority:{x}",filter(lambda x:x%3==0,numbers)),key=lambda l:len(l))
print(result)
print(result1)


numbers = [5, 8, 21, 180, 7, 300, 18]

result = sorted(
    map(lambda x: f"priority:{x}", filter(lambda x: x % 3 == 0, numbers)),
    key=lambda l: int(l.split(":")[1]),  # Extract numeric value and sort
    reverse=True
)

print(result)

