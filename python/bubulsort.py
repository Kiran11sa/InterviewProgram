a = [23,345,78,12,37,14,89,2345,1]
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)