# li = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 10]
# dic={}
# for i in range(min(len(li),len(l2))): #without using dic comprehension
#     dic[li[i]]=l2[i]
# print(dic)
# Using a dictionary comprehension to combine the lists into a dictionary
# dic = {li[i]: l2[i] for i in range(min(len(li), len(l2)))}
# dic = {li[i]: l2[i] for i in range(min(len(li), len(l2)))}

# print(dic)
l=['kiran','kodigela','Rajanna','Ravi']
dic={}
# dic1 = {i:len(i) for i in l}
for i in l:
    dic[i]=len(i)
print(dic)


