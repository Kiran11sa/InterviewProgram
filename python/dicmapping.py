li = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

# Using a dictionary comprehension to combine the lists into a dictionary
dic = {li[i]: l2[i] for i in range(min(len(li), len(l2)))}
# dic = {li[i]: l2[i] for i in range(min(len(li), len(l2)))}

print(dic)
