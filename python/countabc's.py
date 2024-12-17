str_li = "aaaabbbbccccababab"
comp=[]
curr_str=str_li[0]
count=1
for i in range(1,len(str_li)):
    if str_li[i]==curr_str:
       count += 1
    else:
        comp.append(curr_str + str(count))
        curr_str= str_li[i]
        count = 1
comp.append(curr_str+str(count))
comp_str= ''.join(comp)
print(comp_str)
print(comp)
