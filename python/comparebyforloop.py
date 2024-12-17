from selenium.common.exceptions import *

s=[1,2,3,4,5,8]

for i in s:
    if s[i]==4:
        print("a is present in::",i)


# s = "Kiran"
# a = 'a'  # You need to define 'a' before using it in the comparison.
# for i in range(0, len(s)):
#     if s[i] == a:
#         print(f"'{a}' is present at index {i}")
