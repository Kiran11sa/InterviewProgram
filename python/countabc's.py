# str_li = "aaaabbbbccccababab"
# comp=[]
# curr_str=str_li[0]
# count=1
# for i in range(1,len(str_li)):
#     if str_li[i]==curr_str:
#        count += 1
#     else:
#         comp.append(curr_str + str(count))
#         curr_str= str_li[i]
#         count = 1
# comp.append(curr_str+str(count))
# comp_str= ''.join(comp)
# print(comp_str)
# print(comp)

s="aaabbbcccde"
s_l=[]
c_s=s[0]
count=1
for i in range(1,len(s)):
    if s[i]==c_s:
        count+=1
    else:
        s_l.append(c_s+str(count))
        c_s=s[i]
        count=1
s_l.append(c_s+str(count))
s_l1=''.join(s_l)
print(s_l1)
