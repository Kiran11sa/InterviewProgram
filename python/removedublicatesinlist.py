l=[2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)