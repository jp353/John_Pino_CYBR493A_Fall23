def main():
    print()
    if CoolWordsChecker():
        print("Moving to the next functionality")
    else:
        print("You are stuck here")

def CoolWordsChecker():
    """
    This method checks if a user's input matches a predefined password
    :return: True if the password is correct, False otherwise
    """

    secretWord = "EatSh*tPitt"
    userInput = input("Guess the password: ")
    if secretWord == userInput:
        return True
    else:
        print("Wrong Password!")
        return False

if __name__ == "__main__":
    main()



