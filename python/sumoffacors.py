num=12
min_sum=num+1
for i in range(2,int(num**0.5)+1):
    if num %i == 0:
        j=num//i
        min_sum=min(min_sum,i+j)
print(f"min_sim:{min_sum}")