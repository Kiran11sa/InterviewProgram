a=[3,4,6,8,2,9,1]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)