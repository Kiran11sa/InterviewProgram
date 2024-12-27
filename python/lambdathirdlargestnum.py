my_List = [ [3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5] ]
# sorting every sublist of the above list
sort_List = lambda num : ( sorted(n) for n in num )
# Getting the third largest number of the sublist
third_Largest = lambda num, func : [ l[ len(l) - 3] for l in func(num)]
result = third_Largest( my_List, sort_List)
print('The third largest number from every sub list is by using lamda and list comprehension:', result )

l=[ [3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5] ]
l_3=[]
for i in range(0,len(l)):
    l[i].sort()
    # print(l[i])
    # print(l[i][-3])
    l_3.append(l[i][-3])
print("third largest nums of sublist is :",l_3)