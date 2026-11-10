# s = "aaabbbcccdd"
# s_l=[]
# count = 1
# current_s=s[0]
# for i in range(1,len(s)):
#     if current_s==s[i]:
#         count+=1
#     else:
#         s_l.append(current_s+str(count))
#         current_s=s[i]
#         count=1
# s_l.append(current_s+str(count))
# result=''.join(s_l)
# print(result)
# # def foo(i, x):
# #     x.append(i)  # Append `i` to the list
# #     x.append(x.append(i))  # Append `None` because x.append(i) returns None
# #     return x
#
# # y = []  # Initialize an empty list
# # for i in range(3):
# #     y = foo(i, y)  # Pass the list `y` to the function
# # print(y)
# z=[]
# print([z.append(2)])
# print(z)
# from python.comprehension import numbers
# from audioop import error

Input_str = "Pri Version Full:[417.1], Pri Version Full:[417'], Pri Version Full:[41999'],  Pri Version Full:[4.1999'] , Pri Version Full:[0012.232]"
parts =Input_str.replace("["," ").replace(","," ").replace("]"," ").replace("'"," ").split()

print(parts)
numbers = []
for part in parts:
    try:
        num = float(part)
        if num.is_integer():
            numbers.append(str(int(num)))
        else:
            numbers.append(str(num))
    except ValueError:
        pass

print(','.join(numbers))

