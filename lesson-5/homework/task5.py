def is_prime(n):
    """Returns True if n is a prime number, otherwise returns False."""
    if n < 2:  # Prime numbers start from 2
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to √n
        if n % i == 0:
            return False
    return True

# Sample test cases
print(is_prime(2))   # True
print(is_prime(11))  # True
print(is_prime(25))  # False
print(is_prime(29))  # True
print(is_prime(1))   # False