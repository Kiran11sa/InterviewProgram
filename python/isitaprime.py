# n=int(input("enter a number:"))
# if n !=0 and n%2 !=0:
#     print("n is a prime number")
# else:
#     print("n is not a prime number")
n = int(input("Enter a number:"))

# Check if n is less than 2
if n < 2:
    print("n is not a prime number")
else:
    k = True  # Assume n is prime unless proven otherwise

    # Check for divisibility from 2 to the square root of n
    # for i in range(2, n + 1):
    for i in range(2, n):
    # for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            k = False
            break

    if k:
        print("n is a prime number")
    else:
        print("n is not a prime number")


