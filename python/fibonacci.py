# Function to generate Fibonacci series
def generate_fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Number of terms in the Fibonacci series
n = 10  # Change this value to generate a different number of terms

# Generate and print the Fibonacci series
fibonacci_series = generate_fibonacci(n)
print(fibonacci_series)
