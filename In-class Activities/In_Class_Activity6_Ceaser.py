# Defines the alphabet and puts in into a list
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Uses Caesar cipher key 3, so it moves each letter 3 spaces from the original point in the alphabet
key = 3

# Gets user input message and displays prompt for the user
# I was too lazy to get this to work for lowercase letters, so this will have to do.
user_message = input("Give me a word to encrypt! Please be kind and only use uppercase letters! ")

encrypted_user_message = ''

# Looks over the characters in the message and joins them to finish encrypting
# This could probably be done more efficiently with a for loop but this work too
encrypted_user_message = ''.join([letters[(letters.index(char) + key) % len(letters)] if char in letters else char for char in user_message])

# Prints the original message and encrypted message
print("Original message:", user_message)
print("Encrypted message:", encrypted_user_message)
