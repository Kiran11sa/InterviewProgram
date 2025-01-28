list1 = [1,2,3,2,4,5,6]
list2 = [7,8,4,2,2,10]
l=[]
print('count 2 :',list2.count(2))
for x in list1:
    for y in list2:
        if x == y:
            l.append(x)
print("The common element is:",l)
l=[]
print('list:',type(l))
l1={}
print('dic:',type(l1))
l3=()
print('tuple:',type(l3))
l4=set()
print('set:',type(l4))
l5=frozenset()
print('fset:',type(l5))
