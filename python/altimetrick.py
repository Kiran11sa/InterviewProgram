# Count the number of each characters in a given string : "kiran ds testing"
st= "kiran is testing"
dic = {}
for i in st:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
numbers=[1,2,3,4]
sqri=[x*x for x in numbers]
print(sqri)

dict1={"a":22,"b":3, "c":33, "d":10}
sorting_keys= dict(sorted(dict1.items(), key=lambda x: x[1]))
print("!!!!!!!!!!!",dict1.items())
print("@@@@@@",dict1.values())
print(sorting_keys)