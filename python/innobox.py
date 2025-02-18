# Write a functions to get the number value from string

# Output :  417.1, 417, 41999, 4.1999, 0012.23
def extract_numbers(st):
    parts = st.replace("[", " ").replace("]", " ").replace(","," ").replace("'"," ").split()
    numbers =[]
    for part in parts:
        try:
            num = float(part)
            if num.is_integer():
                numbers.append(str(int(num)))
            else:
                numbers.append(str(num))
        except ValueError:
            continue
    return numbers
Input_str = "Pri Version Full:[417.1], Pri Version Full:[417'], Pri Version Full:[41999'],  Pri Version Full:[4.1999'] , Pri Version Full:[0012.232]"
numbers = extract_numbers(Input_str)
print(", ".join(numbers))