# num=int(input("enter a number:"))
# prime=True
# for i in range(2,num):
#     if num%i == 0:
#         prime = False
#         break
# if prime:
#     print("This is a prime number")
# else:
#     print("this is not a prime number")

num=int(input("enter a number:"))
comp=False
for i in range(2,num):
    if num%i != 0:
        prime = True
        break
if prime:
    print("This is a  com number")
else:
    print("this is a not com number")