"""
John Pino
HW #2
9/20/23
CYBR 493A-001
"""

# This program works with the main method located in HW2_Main.py
# It defines 3 methods to work with the password program in the aforementioned file

# This defines a function called "ValidLength" that takes one argument called "password"
def ValidLength(password):
# This checks if the password argument contianes at least 8 characters
    return len(password) >= 8

# This defines the HasNumber function and takes the password argument
def HasNumber(password):
# This will check if there's at least 1 digit in the password
    return any(char.isdigit() for char in password)

# This defined the HasSymbol function that takes the same argument as the others
def HasSymbol(password):

# This defines a list of symbols
    list_of_symbols = "%!@#$%^&*"
# It checks if the password contains at least 1 of the symbols given in the list
    return any(char in list_of_symbols for char in password)
