s = "aaabbbcccdd"
s_l=[]
count = 1
current_s=s[0]
for i in range(1,len(s)):
    if current_s==s[i]:
        count+=1
    else:
        s_l.append(current_s+str(count))
        current_s=s[i]
        count=1
s_l.append(current_s+str(count))
result=''.join(s_l)
print(result)

