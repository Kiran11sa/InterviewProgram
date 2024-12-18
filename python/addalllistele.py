# l=[34,12,23,45,67,1]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

hight = 7
for i in range(1,hight+1):
    spaces = hight - i
    stars = i
    # print( ' '*spaces + " *" * stars)
    print( spaces*' ' + "* " * stars)
    # print( "*" * stars+''*spaces)

