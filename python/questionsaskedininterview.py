# list1 = [1,2,3,4]
# print(list1.pop()) #4
# print(list1) #[1,2,3]
# print(list1.remove(1)) #None
# print(list1) #[2,3]
#
# def foo(i, x):
#     x.append(x.append(i))
#     return x
# # x=[]
#
# for i in range(3):
#     y = foo(i,2)
#     print(y)

# def foo(i, x):
#     x.append(i)  # Append `i` to the list
#     x.append(x.append(i))  # Append `None` because x.append(i) returns None
#     return x
#
# y = []  # Initialize an empty list
# for i in range(3):
#     y = foo(i, y)  # Pass the list `y` to the function
# print(y)

# l1=[2,3,68,6,3,867,789,453,343,22]
# l2=[1,2,3,5,3,7,3]
# unique_list=list(set(l1))
# f_l=unique_list+l2
# total=sum(unique_list)
# print(total)
# l3=[]
# for i in l1:
#     if i not in l3:
#         l3.append(i)
# print(l3)
#--------------------------------------
# n=5
# for i in range(1,n+1):
#     for j in range(n-i+1):
#         print(i,end=' ')
#     print( )
# ----------------------------------
def modify(x):
    x=x+10
    return x
num=3
z=modify(num)
num=4
print(num)
print(z)