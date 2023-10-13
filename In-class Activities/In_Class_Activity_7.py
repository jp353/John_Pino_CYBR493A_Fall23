"""
This program encrypts a message by assigning each letter a value of 1-26
It then multiplies each number by a value determined by the user and displays the output
The number provided by the user can only be between 1-100
"""

# Assigns letters of the alphabet to a variable
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Accepts user input and assigns it as a variable
user_input = input("Please type a single word to encrypt. Only use uppercase letters: ")

key = int(input("Now, give me a number between 1 and 100: "))

# Makes sure the user input number is between 1-100
if 1 <= key <= 100:
    encrypted_user_input = ''

# Iterates through the list
    for char in user_input:
            letter_value = letters.index(char) + 1  # Assigns each letter a value from 1 to 26
            encrypted_value = letter_value * key  # Multiplies the letter's value by the user-provided number
            encrypted_user_input += str(encrypted_value)

    # Prints the original message and the encrypted message
    print("Original message:", user_input)
    print("Encrypted message:", encrypted_user_input)
