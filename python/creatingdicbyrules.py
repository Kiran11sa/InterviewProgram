numbers=[5,8,21,180,7,300,18]
result=sorted(map(lambda x:f"priority:{x}",filter(lambda x:x%3==0,numbers)),key=lambda l:len(l),reverse=True)
print(result)


numbers = [5, 8, 21, 180, 7, 300, 18]

result = sorted(
    map(lambda x: f"priority:{x}", filter(lambda x: x % 3 == 0, numbers)),
    key=lambda l: int(l.split(":")[1]),  # Extract numeric value and sort
    reverse=True
)

print(result)

