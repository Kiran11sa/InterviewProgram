number = int(input("Enter a number: "))

if number <= 1:
    print(f"{number} is not a composite number.")
else:
    is_composite = False
    for i in range(2,number):
    # for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_composite = True
            break

    if is_composite:
        print(f"{number} is a composite number.")
    else:
        print(f"{number} is not a composite number (it may be prime or not valid).")
