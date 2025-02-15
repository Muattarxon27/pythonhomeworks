from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)

    result = []

    # Elements in list1 but not in list2
    for num in count1:
        if num not in count2:
            result.extend([num] * count1[num])  # Preserve count
        elif count1[num] > count2[num]:
            result.extend([num] * (count1[num] - count2[num]))

    # Elements in list2 but not in list1
    for num in count2:
        if num not in count1:
            result.extend([num] * count2[num])  # Preserve count
        elif count2[num] > count1[num]:
            result.extend([num] * (count2[num] - count1[num]))

    return result

# Test cases
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # Output: [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # Output: [2, 2, 5]

def print_squares(n):
    for i in range(1, n):  # Iterates from 1 to n-1
        print(i * i)  # Prints the square of i

# Test case
n = 5
print_squares(n)
def insert_underscore(txt):
    vowels = "aeiou"
    result = []
    i = 0

    while i < len(txt):
        result.append(txt[i])
        
        if (i + 1) % 3 == 0:  # Har uchinchi belgidan keyin
            if i + 1 < len(txt) and (txt[i] in vowels or (result and result[-1] == '_')):
                result.append(txt[i + 1])  # Keyingi belgi qo'shiladi
                i += 1  # Keyingi belgini oldik, indeksni oshiramiz
            
            if i + 1 < len(txt):  # Oxirgi belgi bo'lmasa
                result.append('_')

        i += 1  # Indeksni oshiramiz

    return "".join(result)

# Test misollar
print(insert_underscore("hello"))  # Output: hel_lo
print(insert_underscore("assalom"))  # Output: ass_alom
print(insert_underscore("abcabcdabcdeabcdefabcdefg"))  # Output: abc_abcd_abcdeab_cdef_abcdefg
import random

def play_game():
    number = random.randint(1, 100)  # Generate a random number
    attempts = 10  # Maximum attempts

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print("🎉 You guessed it right! 🎉")
            return  # Exit the game if guessed correctly

    print("😢 You lost. Want to play again? (Y/YES/y/yes/ok) ")
    replay = input().strip().lower()
    
    if replay in ['y', 'yes', 'ok']:
        play_game()  # Restart the game



def check_password():
    password = input("Enter your password: ")  # Foydalanuvchidan parol olish

    if len(password) < 8:
        print("❌ Password is too short.")
    elif not any(char.isupper() for char in password):  # Kamida bitta katta harf borligini tekshirish
        print("❌ Password must contain an uppercase letter.")
    else:
        print("✅ Password is strong.")

# Funktsiyani chaqirish (shart!)
check_password()
print("Prime numbers between 1 and 100:")

for num in range(2, 101):  # Start from 2 (since 1 is not prime)
    is_prime = True  # Assume number is prime

    for divisor in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % divisor == 0:
            is_prime = False
            break  # Exit inner loop if divisible

    if is_prime:
        print(num, end=" ")  # Print prime number