from selenium.common.exceptions import *

s=[1,2,3,4,5,8,4]

for i in range(0,len(s)):
    if s[i]==4:
        print("4 is present in::",i)


# s = "Kirana"
# a = 'a'  # You need to define 'a' before using it in the comparison.
# for i in range(0, len(s)):
#     if s[i] == a:
#         print(f"'{a}' is present at index {i}")
