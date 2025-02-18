# Number of terms in the Fibonacci series
n = int(input("Enter a num:"))  # Change this value to generate a different number of terms

# Initialize the first two terms
a, b = 0, 1
num=[]
num1=[]

# # Print the first two terms
# print(a, end=' ')
# print(b, end=' ')

# Generate and print the remaining terms
for i in range(n):
    num.append(a)
    a, b = b, a + b
    # num1.append(a)

print(num)
print(num1)
