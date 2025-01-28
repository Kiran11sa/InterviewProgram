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
# def foo(i, x):
#     x.append(i)  # Append `i` to the list
#     x.append(x.append(i))  # Append `None` because x.append(i) returns None
#     return x

# y = []  # Initialize an empty list
# for i in range(3):
#     y = foo(i, y)  # Pass the list `y` to the function
# print(y)
z=[]
print([z.append(2)])
print(z)



