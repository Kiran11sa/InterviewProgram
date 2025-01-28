num=13
min_sum=num+1
for i in range(2,int(num**0.5)+1):
    if num %i == 0:
        j=num//i
        min_sum=min(min_sum,i+j)
print(f"min_sum:{min_sum}")
import random
import string
def randoms():
    mail=''.join(random.choices(string.ascii_lowercase + string.digits,k=9))
    domains=['gmail.com','yahoo.com','email.com']
    domain=random.choice(domains)
    email=mail+'@'+domain
    return email
res=randoms()
print(res)

