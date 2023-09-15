def main():
    print()
    strTemp = "="
    if CoolWordsChecker() == True:
        print("Moving to next functionality")
    else:
        print("You are stuck here")


def WordsChecker():...


def CoolWordsChecker():
    """
This method checks if a user's input matches a pre-defined password
    :return:
    """

    secretWord = "EatSh*tPitt"
    userInput = input("Guess the password")
    if (secretWord == userInput):
        return True
    else:
        return False


        print("Wrong Password!")



if __name__ == "__main__" :
    main()



