# list1 = [1,2,3,4]
# print(list1.pop())
# print(list1)
# print(list1.remove(1))
# print(list1)

def foo(i, x):
    x.append(x.append(i))
    return x


for i in range(3):
    y = foo(i,2)
    print(y)