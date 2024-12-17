# li=[12,34,56,87,23]
# li.sort()
# print(li)
# print(li[-2])
# s=input("Enter s string:")
# rev=s[::-1]
# if s==rev:
#     print("s is palindrom")
# else:
#     print("s is not pal ")
# num=int(input("enter a num:"))
# if num %2==0:
#     print("num is even")
# else:
#     print("number is  odd")
f=1
L=100
even=[]
odd=[]
for i in range(f,L+1):
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"list of even:", even)
print(f"list of odd:",odd)
