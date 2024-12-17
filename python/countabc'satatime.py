import time
st="aabbaacchhffkk"
li=[]
cur_str=st[0]
count=1
for i in range(1,len(st)):
    if cur_str == st[i]:
        count +=1

    else:
        li.append(cur_str +str(count))
        cur_str=st[i]
        count=1
li.append(cur_str +str(count))
result=''.join(li)
print(result)
print(li)
