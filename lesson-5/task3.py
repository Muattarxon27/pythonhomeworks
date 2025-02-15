def find_factors(n):
    """Prints all factors of a given number n."""
    for i in range(1, n + 1):  # Iterate from 1 to n
        if n % i == 0:  # Check if i is a factor of n
            print(f"{i} is a factor of {n}")

# Get user input
num = int(input("Enter a positive integer: "))

# Validate input
if num > 0:
    find_factors(num)
else:
    print("Please enter a positive integer!")