"""
This is the main screen for Homework #2. Do not make any changes to this file.
"""
# import the necessary files (your folder should be named Homeworks)
from Homeworks import HW2


def main():
    """
        The main method accepts data from user and passes it to the HW2 class.
        A valid password is a password that is at least 8 characters long, has at least one number, and one symbol.
    """


# Accept password from user
password = input("Give me a password to check")
# Check whether it is a valid password or not
if HW2.ValidLength(password) == True and HW2.HasNumber(password) == True and HW2.HasSymbol(password) == True:
    print("Valid password")
else:
    print("Invalid Password")

if __name__ == "__main__":
    main()